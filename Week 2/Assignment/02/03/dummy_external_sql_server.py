import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Dummy External SQL API Server')
conn = sqlite3.connect('external_repo.db', check_same_thread=False)
conn.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, author TEXT, title TEXT, content TEXT)')
conn.commit()

class SQLReq(BaseModel):
    sql: str
    params: list = []

@app.post('/sql/execute')
def execute(req: SQLReq):
    cur = conn.cursor()
    cur.execute(req.sql, tuple(req.params))
    if req.sql.strip().lower().startswith('select'):
        cols = [d[0] for d in cur.description]
        rows = [dict(zip(cols, r)) for r in cur.fetchall()]
        return {'rows': rows}
    conn.commit()
    return {'rowcount': cur.rowcount, 'lastrowid': cur.lastrowid}
