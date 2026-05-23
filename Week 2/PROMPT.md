# Week 2 학습/과제/딥다이브 실행 프롬프트 (정제본)

## 목표
- Week 2 수업 내용을 구조적으로 정리한다.
- Assignment를 단계적으로 수행하며 백엔드 복잡도 확장을 체감한다.
- DeepDive를 통해 HTTPS, Pydantic, 예외처리, 비동기, CORS를 코드와 문서로 심화 탐구한다.

## 디렉터리 규칙
- `Week 2/README.md`: 주차 핵심 키워드/학습 요약
- `Week 2/Assignment/README.md`: 과제 인덱스
- `Week 2/DeepDive/README.md`: 딥다이브 인덱스
- 각 숫자 폴더는 반드시 `README.md` 포함

## Assignment 요구사항
1. HTTP 핵심 키워드 심층 정리 (`Assignment/01/README.md`)
2. FastAPI 커뮤니티 백엔드 단계별 고도화 (`Assignment/02/01~05`)
   - 01: REST API + 인메모리 DB
   - 02: AI 채팅 API + OpenAI/로컬 호환 + 폴백 응답
   - 03: 외부 DB 연동 + 실패 시 인메모리 폴백
   - 04: Route-Controller-Model 리팩토링
   - 05: 실행 가능한 백엔드 + Streamlit 테스트 UI

## DeepDive 요구사항
1. HTTPS 전제 REST API 재설계 + 구현 (`DeepDive/01/https_rest_api`)
2. Pydantic 전면 검증 적용 (`DeepDive/02/community_backend_with_pydantic_model`)
3. 기본/커스텀 예외 + 안정성 모니터 (`DeepDive/03/...`)
4. async/await 전환 + API 비교 테스트 도구 (`DeepDive/04/...`)
5. CORS 트러블 시나리오 HTML/CSS/JS 구현 (`DeepDive/05`)

## 산출물 품질 기준
- README는 “무엇/왜/어떻게/실행법/검증법”을 포함
- 코드 예시는 바로 실행 가능한 최소 단위로 제공
- 단계별 변경점은 이전 단계 대비 관점으로 명시
