
# DeepDive 01 - HTTPS REST API 재설계

## 핵심 분석
- **암호화**: TLS 전제(애플리케이션 단에서는 HTTPS 종단 뒤 요청 처리)
- **무결성**: `X-Timestamp + body`를 HMAC-SHA256으로 서명
- **인증**: `X-API-Key` 검증

## 실행
```bash
cd "Week 2/DeepDive/01/https_rest_api"
uvicorn main:app --reload --port 8201
```
