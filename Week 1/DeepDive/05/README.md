# DeepDive 05 - 이터레이터/제너레이터 메모리 효율 실험

## 시나리오
대규모 로그 파일에서 특정 패턴을 스캔할 때, 파일 전체를 메모리에 적재하지 않고 한 줄씩 소비하면 메모리 피크를 줄일 수 있다.

## 과제2 코드와의 연결
- `Assignment/02/week1_cli_pkg/storage.py`의 `iter_lines()`가 지연 평가 방식으로 줄 단위 처리 수행

## 실험 구성
- `experiment.sh`: 더미 대용량 로그 생성 + 간단 벤치마크 결과 파일 생성
- `monitor.py`: 결과 파일 파싱 후 수치 출력

## 실행
```bash
cd "Week 1/Assignment/02"
pip install -e .
cd ../../DeepDive/05
bash experiment.sh 100000 benchmark_result.txt
python3 monitor.py
```

## 예시 출력 화면
```text
=== Memory/Time Monitor ===
log_size: 100000.0
sync_elapsed: ...
sync_mem_kb: ...
gen_elapsed: ...
gen_mem_kb: ...
```
