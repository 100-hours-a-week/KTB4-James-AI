# Assignment 02-05 (최종)

2-3 최신 코드(LLM Gateway + Repo 3옵션)를 기반으로 CORS를 추가한 실행형 통합본입니다.

## 실행
```bash
cd "Week 2/Assignment/02/05"
uvicorn app:app --reload --port 8105
```

Repo 옵션:
- `REPO_MODE=inmemory|internal|external`
- internal: `INTERNAL_DB_PATH`
- external: `EXTERNAL_SQL_API_URL`
