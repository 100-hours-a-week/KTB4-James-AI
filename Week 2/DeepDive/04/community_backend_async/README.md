
# community_backend_async

비동기 적용 API:
- `POST /posts`
- `GET /posts`
- `POST /posts/{post_id}/comments`
- `POST /posts/{post_id}/reactions/{emoji}`
- `POST /ai/chat`

실행:
```bash
uvicorn main:app --reload --port 8204
```
