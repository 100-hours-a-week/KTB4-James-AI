
# Assignment 02-01

## 목표
- 커뮤니티 기본 기능(글/댓글/리액션) REST API 초기 설계
- 인메모리 저장소로 빠른 기능 검증

## 실행
```bash
cd "Week 2/Assignment/02/01"
uvicorn main:app --reload --port 8101
```

## API 목록
| Method | Path | 설명 |
|---|---|---|
| GET | `/health` | 서버 상태 |
| POST | `/posts` | 게시글 생성 |
| GET | `/posts` | 게시글 목록 |
| POST | `/posts/{post_id}/comments` | 댓글 생성 |
| GET | `/posts/{post_id}/comments` | 댓글 목록 |
| POST | `/posts/{post_id}/reactions/{emoji}` | 리액션 추가 |

## 코드 발췌
```python
@app.post('/posts/{post_id}/reactions/{emoji}')
def react(post_id: int, emoji: str):
    if post_id not in posts: raise HTTPException(404, 'post not found')
    reactions[post_id][emoji] = reactions[post_id].get(emoji, 0) + 1
    return {'post_id': post_id, 'reactions': reactions[post_id]}
```
