
# DeepDive 05 - CORS 트러블슈팅

## 실행
프론트 정적 서버:
```bash
cd "Week 2/DeepDive/05/cors_troubleshooting_frontend"
python -m http.server 8305
```
브라우저: `http://localhost:8305`

백엔드(예시):
```bash
cd "Week 2/DeepDive/04/community_backend_async"
uvicorn main:app --reload --port 8204
```

## 시나리오
- Simple request
- Credentials 포함 POST
- Preflight 실패/허용 헤더 불일치 분석
