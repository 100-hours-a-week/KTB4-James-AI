
# https_rest_api 실행/호출

## 실행
```bash
uvicorn main:app --reload --port 8201
```

## 호출 시 필요한 헤더
- `X-API-Key`
- `X-Timestamp`
- `X-Signature`

## 예시 요청 흐름
1) 요청 바디 JSON 생성
2) `timestamp.body` 문자열 HMAC 생성
3) 헤더와 함께 `POST /secure/posts` 호출
