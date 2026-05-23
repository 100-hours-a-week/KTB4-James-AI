# Assignment 02-03 (2-2 기반 누적 + 3중 Repo 옵션)

## 핵심 변경
기존 글로벌 변수 조작 방식 대신 `Repo` 구현체를 통해서만 `create_post/list_posts`가 동작하도록 수정했습니다.

## Repo 3가지 옵션
| 모드 | 클래스 | 동작 |
|---|---|---|
| inmemory | `InMemoryRepo` | 프로세스 메모리 기반 |
| internal | `InternalRepo` | SQLite 파일 DB에 SQL 실행 |
| external | `ExternalRepo` | 외부 SQL API 서버에 내부 HTTP 요청으로 SQL 실행 |

## 실행
```bash
cd "Week 2/Assignment/02/03"
# 1) inmemory
REPO_MODE=inmemory uvicorn main:app --reload --port 8103

# 2) internal(sqlite)
REPO_MODE=internal INTERNAL_DB_PATH=community_internal.db uvicorn main:app --reload --port 8103

# 3) external(sql api)
uvicorn dummy_external_sql_server:app --reload --port 9300
REPO_MODE=external EXTERNAL_SQL_API_URL='http://127.0.0.1:9300/sql/execute' uvicorn main:app --reload --port 8103
```
