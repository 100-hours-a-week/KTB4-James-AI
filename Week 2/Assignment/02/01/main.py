
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, List

app = FastAPI(title='Community API Step 2-1')

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
def health(): return {'status': 'ok', 'step': '2-1'}

@app.post('/posts')
def create_post(data: PostIn):
    pid = seq['post']; seq['post'] += 1
    post = {'id': pid, **data.model_dump()}
    posts[pid] = post; comments[pid] = []; reactions[pid] = {}
    return post

@app.get('/posts')
def list_posts(): return list(posts.values())

@app.post('/posts/{post_id}/comments')
def add_comment(post_id: int, data: CommentIn):
    if post_id not in posts: raise HTTPException(404, 'post not found')
    cid = seq['comment']; seq['comment'] += 1
    row = {'id': cid, **data.model_dump()}; comments[post_id].append(row); return row

@app.get('/posts/{post_id}/comments')
def list_comments(post_id: int):
    if post_id not in posts: raise HTTPException(404, 'post not found')
    return comments[post_id]

@app.post('/posts/{post_id}/reactions/{emoji}')
def react(post_id: int, emoji: str):
    if post_id not in posts: raise HTTPException(404, 'post not found')
    reactions[post_id][emoji] = reactions[post_id].get(emoji, 0) + 1
    return {'post_id': post_id, 'reactions': reactions[post_id]}
