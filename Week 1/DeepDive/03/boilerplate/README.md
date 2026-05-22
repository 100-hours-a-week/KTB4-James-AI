# Boilerplate - 협업 코드에서 타입 힌트 관찰

## 폴더 구조
- `src/collab_app/domain.py`: 도메인 모델/프로토콜
- `src/collab_app/service.py`: 비즈니스 로직
- `src/collab_app/infrastructure.py`: 외부 데이터 소스 mock
- `tests/test_service.py`: 동작 검증

## 디버깅/유지보수 영향
- 인터페이스(`Protocol`)로 구현 교체가 쉬워짐
- `TypedDict`로 JSON 유사 데이터 구조를 명시해 오타 감소
- 타입 기반 리팩토링 시 IDE 네비게이션 품질 향상

## 타입 힌트 한계 시연 포인트
- 런타임에는 타입 미강제 → 수동 검증 함수 필요
- `cast` 오용 시 정적 검사 통과 후 런타임 오류 가능
