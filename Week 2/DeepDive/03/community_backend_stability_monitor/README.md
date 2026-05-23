
# community_backend_stability_monitor

## 실행
```bash
bash monitor.sh http://localhost:8203
```

## 출력 예시
- `/ai/predict -> 200`
- `/ai/predict?mode=fail -> 503`
- `/db/write -> 200`
- `/db/write?mode=fail -> 503`
