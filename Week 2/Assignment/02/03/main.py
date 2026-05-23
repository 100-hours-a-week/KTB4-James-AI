import json
import os
import random
import sqlite3
from pathlib import Path
from typing import Literal, Protocol
from urllib import request

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title='Community API Step 2-3')
FALLBACK = ['현재 모델 연결이 원활하지 않습니다.', '잠시 후 다시 시도해주세요.', '기본 응답으로 대체합니다.']

# ---------- schemas ----------
class PostIn(BaseModel):
    author: str = Field(min_length=2, max_length=30)
    title: str = Field(min_length=1, max_length=120)
    content: str = Field(min_length=1, max_length=5000)

class ChatRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=2000)
    model: str = 'gpt-4.1-mini'
    temperature: float = Field(default=0.7, ge=0, le=2)
    max_tokens: int = Field(default=256, ge=1, le=2048)

class LLMGatewayConfig(BaseModel):
    backend: Literal['local', 'cloud']
    local_base_url: str = 'http://127.0.0.1:9200/v1/chat/completions'
    cloud_base_url: str = 'https://api.openai.com/v1/chat/completions'
    cloud_api_key: str | None = None

class DBConfig(BaseModel):
    mode: Literal['inmemory', 'internal', 'external'] = 'inmemory'
    internal_db_path: str = 'community_internal.db'
    external_sql_api_url: str = 'http://127.0.0.1:9300/sql/execute'

LLM_CONFIG = LLMGatewayConfig(
    backend=os.getenv('LLM_BACKEND', 'local'),
    local_base_url=os.getenv('LOCAL_LLM_URL', 'http://127.0.0.1:9200/v1/chat/completions'),
    cloud_base_url=os.getenv('CLOUD_LLM_URL', 'https://api.openai.com/v1/chat/completions'),
    cloud_api_key=os.getenv('OPENAI_API_KEY'),
)
DB_CONFIG = DBConfig(
    mode=os.getenv('REPO_MODE', 'inmemory'),
    internal_db_path=os.getenv('INTERNAL_DB_PATH', 'community_internal.db'),
    external_sql_api_url=os.getenv('EXTERNAL_SQL_API_URL', 'http://127.0.0.1:9300/sql/execute'),
)

# ---------- utils ----------
def _post_json(url: str, payload: dict, headers: dict | None = None) -> dict:
    req = request.Request(
        url=url,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json', **(headers or {})},
        method='POST',
    )
    with request.urlopen(req, timeout=8) as resp:
        return json.loads(resp.read().decode('utf-8'))

# ---------- repo layer ----------
class Repo(Protocol):
    def create_post(self, row: dict) -> dict: ...
    def list_posts(self) -> list[dict]: ...

class InMemoryRepo:
    def __init__(self) -> None:
        self.posts: list[dict] = []
        self.seq = 1

    def create_post(self, row: dict) -> dict:
        new = {'id': self.seq, **row}
        self.seq += 1
        self.posts.append(new)
        return new

    def list_posts(self) -> list[dict]:
        return self.posts

class InternalRepo:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        conn.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, author TEXT, title TEXT, content TEXT)')
        conn.commit(); conn.close()

    def create_post(self, row: dict) -> dict:
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute('INSERT INTO posts(author, title, content) VALUES (?, ?, ?)', (row['author'], row['title'], row['content']))
        conn.commit()
        post_id = cur.lastrowid
        conn.close()
        return {'id': post_id, **row}

    def list_posts(self) -> list[dict]:
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute('SELECT id, author, title, content FROM posts ORDER BY id DESC')
        rows = [{'id': r[0], 'author': r[1], 'title': r[2], 'content': r[3]} for r in cur.fetchall()]
        conn.close()
        return rows

class ExternalRepo:
    def __init__(self, sql_api_url: str) -> None:
        self.sql_api_url = sql_api_url

    def _exec_sql(self, sql: str, params: list | None = None) -> dict:
        return _post_json(self.sql_api_url, {'sql': sql, 'params': params or []})

    def create_post(self, row: dict) -> dict:
        res = self._exec_sql(
            'INSERT INTO posts(author, title, content) VALUES (?, ?, ?)',
            [row['author'], row['title'], row['content']],
        )
        return {'id': res.get('lastrowid', 0), **row, 'source': 'external-sql-api'}

    def list_posts(self) -> list[dict]:
        res = self._exec_sql('SELECT id, author, title, content FROM posts ORDER BY id DESC')
        return res.get('rows', [])


def get_repo() -> tuple[str, Repo]:
    if DB_CONFIG.mode == 'external':
        return 'external', ExternalRepo(DB_CONFIG.external_sql_api_url)
    if DB_CONFIG.mode == 'internal':
        return 'internal', InternalRepo(DB_CONFIG.internal_db_path)
    return 'inmemory', InMemoryRepo()

repo_mode, repo = get_repo()

# ---------- APIs ----------
@app.get('/health')
def health():
    return {'status': 'ok', 'step': '2-3', 'repo_mode': repo_mode, 'llm_backend': LLM_CONFIG.backend}

@app.post('/posts')
def create_post(data: PostIn):
    return repo.create_post(data.model_dump())

@app.get('/posts')
def list_posts():
    return repo.list_posts()

@app.post('/ai/chat')
def chat(req: ChatRequest):
    payload = {
        'model': req.model,
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': req.prompt}],
        'temperature': req.temperature,
        'max_tokens': req.max_tokens,
    }
    try:
        if LLM_CONFIG.backend == 'local':
            raw = _post_json(LLM_CONFIG.local_base_url, payload)
            return {'backend': 'local', 'answer': raw['choices'][0]['message']['content'], 'raw': raw}
        if not LLM_CONFIG.cloud_api_key:
            return {'backend': 'fallback', 'answer': random.choice(FALLBACK), 'reason': 'missing OPENAI_API_KEY'}
        raw = _post_json(LLM_CONFIG.cloud_base_url, payload, {'Authorization': f'Bearer {LLM_CONFIG.cloud_api_key}'})
        return {'backend': 'cloud', 'answer': raw['choices'][0]['message']['content'], 'raw': raw}
    except Exception as e:
        return {'backend': 'fallback', 'answer': random.choice(FALLBACK), 'reason': str(e)}
