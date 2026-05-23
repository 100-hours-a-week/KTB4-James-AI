# Assignment 02-02

## 02-01 대비 추가점
- 기존 커뮤니티 API(글/댓글/리액션) 유지
- AI 서빙을 **클라이언트 위임 방식**이 아니라 **백엔드 내부 게이트웨이 정책**으로 재설계
- OpenAI 호환 표준 요청 스키마(`model/messages/temperature/max_tokens`)로 Local/Cloud를 동일 호출 형태로 처리

## 핵심 설계
- 클라이언트는 `prompt`, `model`, `temperature`, `max_tokens`만 전달
- 백엔드가 `LLM_BACKEND` 환경변수(`local|cloud`)로 경로를 결정
- Local/Cloud 모두 `/v1/chat/completions` 형태의 표준 API를 호출
- 장애/설정누락 시 fallback 응답 반환

## [로컬 모델 적용 가이드]
### 1) 더미 로컬 AI 코어 서버 실행
```bash
cd "Week 2/Assignment/02/02"
uvicorn dummy_local_llm_server:app --reload --port 9200
```

### 2) 백엔드 실행(로컬 모드)
```bash
cd "Week 2/Assignment/02/02"
LLM_BACKEND=local LOCAL_LLM_URL='http://127.0.0.1:9200/v1/chat/completions' \
uvicorn main:app --reload --port 8102
```

### 3) 요청
```bash
curl -X POST http://127.0.0.1:8102/ai/chat \
  -H 'content-type: application/json' \
  -d '{"prompt":"로컬모델 테스트","model":"local-7b","temperature":0.4,"max_tokens":128}'
```

## [상용 클라우드 모델 적용 가이드]
### 1) 환경변수 설정
```bash
export LLM_BACKEND=cloud
export OPENAI_API_KEY='YOUR_KEY'
# 필요 시
export CLOUD_LLM_URL='https://api.openai.com/v1/chat/completions'
```

### 2) 백엔드 실행
```bash
cd "Week 2/Assignment/02/02"
uvicorn main:app --reload --port 8102
```

### 3) 요청
```bash
curl -X POST http://127.0.0.1:8102/ai/chat \
  -H 'content-type: application/json' \
  -d '{"prompt":"cloud 테스트","model":"gpt-4.1-mini","temperature":0.7,"max_tokens":128}'
```

## 코드 포인트
```python
if CONFIG.backend == 'local':
    raw = _post_json(CONFIG.local_base_url, payload)
elif CONFIG.backend == 'cloud':
    raw = _post_json(CONFIG.cloud_base_url, payload, headers={'Authorization': f'Bearer {CONFIG.cloud_api_key}'})
```
