# Threat Model

This project models abnormal behavior patterns rather than specific attacks.

## Assets Considered

- Network activity logs
- System event logs
- Authentication records (synthetic)

## Threat Categories (Conceptual)

- Sudden traffic bursts
- Unusual access frequency
- Repeated failed operations
- Automation-like timing patterns

## What Is NOT Modeled

- Malware payloads
- Exploit techniques
- Command-and-control traffic
- Lateral movement

## Risk of Misinterpretation

Behavioral deviation does not imply malicious intent.
Legitimate system changes may trigger anomalies.

False positives are expected and acceptable in this model.
