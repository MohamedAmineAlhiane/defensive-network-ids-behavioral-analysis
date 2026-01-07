# Assumptions

This system operates under several explicit assumptions to ensure that
behavioral analysis remains meaningful and ethically scoped.

## Data Assumptions

- Input events are pre-collected logs, not live traffic.
- Timestamps are assumed to be in ISO 8601 format.
- Events represent normal and abnormal behavior mixed together.
- Data quality may be imperfect; missing or malformed fields are tolerated.

## Behavioral Assumptions

- Past behavior is a reasonable approximation of future "normal" behavior.
- Sudden deviations in frequency or timing may indicate abnormal conditions,
  but not necessarily malicious intent.
- No single signal is sufficient to determine risk.

## Operational Assumptions

- This system is intended for offline or batch analysis.
- Human analysts are expected to interpret results.
- Automated enforcement is explicitly out of scope.
