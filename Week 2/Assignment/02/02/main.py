import os, random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, List, Literal
from urllib import request
import json

app = FastAPI(title='Community API Step 2-2')
FALLBACK = ['현재 모델 연결이 원활하지 않습니다.', '잠시 후 다시 시도해주세요.', '기본 응답으로 대체합니다.']

# ---------- community APIs from 2-1 ----------
class PostIn(BaseModel):
    author: str = Field(min_length=2, max_length=30)
    title: str = Field(min_length=1, max_length=120)
    content: str = Field(min_length=1, max_length=5000)
class CommentIn(BaseModel):
    author: str = Field(min_length=2, max_length=30)
    content: str = Field(min_length=1, max_length=1000)

posts: Dict[int, dict] = {}
comments: Dict[int, List[dict]] = {}
reactions: Dict[int, Dict[str, int]] = {}
seq = {'post': 1, 'comment': 1}

@app.get('/health')
def health():
    return {'status': 'ok', 'step': '2-2', 'llm_backend': os.getenv('LLM_BACKEND', 'local')}

@app.post('/posts')
def create_post(data: PostIn):
    pid=seq['post']; seq['post']+=1
    row={'id':pid, **data.model_dump()}
    posts[pid]=row; comments[pid]=[]; reactions[pid]={}
    return row

@app.get('/posts')
def list_posts(): return list(posts.values())

@app.post('/posts/{post_id}/comments')
def add_comment(post_id:int,data:CommentIn):
    if post_id not in posts: raise HTTPException(404,'post not found')
    cid=seq['comment']; seq['comment']+=1
    row={'id':cid, **data.model_dump()}; comments[post_id].append(row)
    return row

@app.post('/posts/{post_id}/reactions/{emoji}')
def react(post_id:int,emoji:str):
    if post_id not in posts: raise HTTPException(404,'post not found')
    reactions[post_id][emoji]=reactions[post_id].get(emoji,0)+1
    return {'post_id':post_id,'reactions':reactions[post_id]}

# ---------- standardized AI gateway ----------
class ChatRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=2000)
    model: str = Field(default='gpt-4.1-mini')
    temperature: float = Field(default=0.7, ge=0, le=2)
    max_tokens: int = Field(default=256, ge=1, le=2048)

class LLMStandardRequest(BaseModel):
    model: str
    messages: list[dict]
    temperature: float
    max_tokens: int

class LLMGatewayConfig(BaseModel):
    backend: Literal['local','cloud']
    local_base_url: str = 'http://127.0.0.1:9200/v1/chat/completions'
    cloud_base_url: str = 'https://api.openai.com/v1/chat/completions'
    cloud_api_key: str | None = None

CONFIG = LLMGatewayConfig(
    backend=os.getenv('LLM_BACKEND','local'),
    local_base_url=os.getenv('LOCAL_LLM_URL','http://127.0.0.1:9200/v1/chat/completions'),
    cloud_base_url=os.getenv('CLOUD_LLM_URL','https://api.openai.com/v1/chat/completions'),
    cloud_api_key=os.getenv('OPENAI_API_KEY')
)

def _to_standard_payload(chat: ChatRequest) -> dict:
    req = LLMStandardRequest(
        model=chat.model,
        messages=[{'role':'system','content':'You are a helpful assistant.'},{'role':'user','content':chat.prompt}],
        temperature=chat.temperature,
        max_tokens=chat.max_tokens
    )
    return req.model_dump()

def _post_json(url: str, payload: dict, headers: dict | None = None) -> dict:
    data = json.dumps(payload).encode('utf-8')
    req = request.Request(url=url, data=data, headers={'Content-Type':'application/json', **(headers or {})}, method='POST')
    with request.urlopen(req, timeout=8) as resp:
        return json.loads(resp.read().decode('utf-8'))

def _extract_text(resp: dict) -> str:
    # OpenAI-compatible format
    try:
        return resp['choices'][0]['message']['content']
    except Exception:
        return random.choice(FALLBACK)

@app.post('/ai/chat')
def chat(req: ChatRequest):
    payload = _to_standard_payload(req)
    try:
        if CONFIG.backend == 'local':
            raw = _post_json(CONFIG.local_base_url, payload)
            return {'backend':'local','answer':_extract_text(raw),'raw':raw}
        if not CONFIG.cloud_api_key:
            return {'backend':'fallback','answer':random.choice(FALLBACK),'reason':'missing OPENAI_API_KEY'}
        raw = _post_json(CONFIG.cloud_base_url, payload, headers={'Authorization':f'Bearer {CONFIG.cloud_api_key}'})
        return {'backend':'cloud','answer':_extract_text(raw),'raw':raw}
    except Exception as e:
        return {'backend':'fallback','answer':random.choice(FALLBACK),'reason':str(e)}
