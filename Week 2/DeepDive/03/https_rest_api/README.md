
# HTTPS 변환 노트

Assignment 2-1의 HTTP API를 HTTPS 가정으로 전환할 때,
- API Key 인증,
- Timestamp + Signature 검증,
- TLS 종료 위치(Reverse Proxy) 분리
를 적용하는 방식으로 보안 요구(암호화/무결성/인증)를 충족한다.
