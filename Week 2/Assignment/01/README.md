# Assignment 01 - HTTP 내용 정리

## 핵심 키워드
- Stateless, Method Semantics, Header/Body
- 상태코드(2xx/4xx/5xx), 캐시, 콘텐츠 협상
- Keep-Alive, 멱등성, 안전성
- HTTPS(TLS): 기밀성/무결성/인증

## 웹 구조 관점 정리
HTTP는 애플리케이션 계층 프로토콜이며, TCP 위에서 요청/응답 모델로 동작한다. REST API 설계에서 URI는 리소스 중심, 메서드는 행위 중심으로 분리하고, 인증은 토큰/세션 전략을 상황별로 선택한다.
