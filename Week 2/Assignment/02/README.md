
# Assignment 02 - 단계별 누적 구현 가이드

아래 단계는 **이전 단계 기능을 유지한 채 누적**됩니다.

| 단계 | 핵심 추가 기능 | 실행 포트 | 확인 API |
|---|---|---:|---|
| 02/01 | 게시글/댓글/리액션 인메모리 REST | 8101 | `GET /health`, `POST /posts` |
| 02/02 | AI 채팅(OpenAI/Local/Fallback) | 8102 | `POST /ai/chat` |
| 02/03 | 외부 DB 어댑터 + 실패 시 인메모리 fallback | 8103 | `GET /health`의 `storage` |
| 02/04 | Route-Controller-Model 구조 리팩토링 | 8104 | `/posts` 라우팅 확인 |
| 02/05 | 최종 통합 + Streamlit UI 테스트 | 8105 | `/health`, `/posts`, `/ai/chat` |

## 공통 실행
```bash
uvicorn main:app --reload --port <포트>
```
(02/05는 `uvicorn app:app --reload --port 8105`)
