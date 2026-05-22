# Week 1 작업 요약 (PR 마무리 보고)

## 1) 요청 이행 요약
- `Week 1` 학습/과제/딥다이브 구조를 생성하고, 정제 프롬프트를 `PROMPT.md`로 기록.
- 과제 1(동기 CLI) 구현 + 설계/예외처리 문서화.
- 과제 2(패키지 리팩토링) 구현 + 타입 힌트/제너레이터 도입 및 철학 문서화.
- 딥다이브 01~05 보고서 및 부가 코드(boilerplate, 실험 스크립트, 모니터링 CLI) 작성.
- 후속 피드백 반영: 불필요한 `pyc/__pycache__` 전량 제거 및 `.gitignore` 추가.

## 2) 디렉터리/문서 구성
- `Week 1/README.md`: 1주차 학습 키워드 총정리
- `Week 1/PROMPT.md`: 정제된 실행 프롬프트
- `Week 1/Assignment/README.md`: 과제 목차
- `Week 1/Assignment/01/README.md`: 과제1 설계 및 사용 가이드
- `Week 1/Assignment/02/README.md`: 과제2 리팩토링 철학 및 설치/실행 가이드
- `Week 1/DeepDive/README.md`: 딥다이브 목차
- `Week 1/DeepDive/01~05/README.md`: 주제별 보고서
- `Week 1/DeepDive/03/boilerplate/README.md`: 협업형 타입 힌트 관찰용 프로젝트 안내

## 3) 구현 요약
### Assignment 01
- 파일: `Assignment/01/cli_study_tracker.py`
- 핵심:
  - 메뉴 루프(`while True`) + 분기(`if/elif`) 기반 CLI
  - `input()/print()` 중심 인터랙션
  - `ValueError`, `EOFError`, `KeyboardInterrupt` 처리
  - Guard Clause 기반 입력 검증

### Assignment 02
- 파일: `Assignment/02/week1_cli_pkg/*`, `Assignment/02/pyproject.toml`
- 핵심:
  - 모듈 분리(`models.py`, `storage.py`, `main.py`)
  - 콘솔 엔트리포인트(`week1-study`) 제공
  - 타입 힌트 적용
  - `iter_lines()` 제너레이터로 줄 단위 지연 처리

### DeepDive
- 01: 파이썬 vs 타 언어(초급자 관점 장단점)
- 02: 과제1의 조건문/반복문 발췌 및 동작 해설
- 03: 타입 힌트 적용 분류/영향/한계 + boilerplate 코드
- 04: checked 예외 부재 환경의 예외 처리 설계 분석
- 05: 대용량 처리 시나리오 + `experiment.sh` + `monitor.py`

## 4) 피드백 반영 사항
- 사용자 요청에 따라 `.pyc` 및 `__pycache__`가 런타임 재생성 산출물임을 검토하고 저장소에서 제거.
- 재추적 방지를 위해 루트 `.gitignore` 추가:
  - `__pycache__/`
  - `*.py[cod]`

## 5) 실행/검증 이력
- CLI 기본 흐름 확인:
  - `python3 'Week 1/Assignment/01/cli_study_tracker.py'` (입력 `4`로 종료)
- 문법 컴파일 확인:
  - `python3 -m compileall 'Week 1'`
- 캐시 파일 정리 확인:
  - `find . -type f -name '*.pyc'`

## 6) PR 마무리 상태
- 변경 사항 커밋 완료.
- PR 메시지 기록 도구(`make_pr`) 호출 완료.
- 본 `SUMMARY.md` 추가로 작업 보고 내역을 저장소 내에서 추적 가능하도록 마무리.
