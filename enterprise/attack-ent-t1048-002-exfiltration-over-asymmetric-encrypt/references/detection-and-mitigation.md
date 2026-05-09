# Detection and Mitigation Notes

## Technique

- ATT&CK ID: T1048.002
- Name: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
- Domain: enterprise
- Tactics: exfiltration
- Platforms: ESXi, Linux, macOS, Windows

## ATT&CK detection guidance

No ATT&CK detection guidance was present in the source STIX object.

## Telemetry checklist

- Not specified in the STIX object.

## Mitigation candidates

- Data Loss Prevention
- Filter Network Traffic
- Network Intrusion Prevention
- Network Segmentation

## Triage questions

- What asset, identity, workload, application, or control-plane component is in scope?
- Which observed events directly align with the ATT&CK behavior, and which are only circumstantial?
- What telemetry is missing, delayed, filtered, or known to be unreliable?
- Is this a single event, repeated pattern, campaign-level behavior, or expected administrative activity?
- What compensating controls should have prevented, detected, or limited the behavior?

## False-positive considerations

- Authorized administration, software deployment, security tooling, backup activity, and automated platform maintenance can resemble ATT&CK behavior.
- Before escalating, compare command lineage, account ownership, change tickets, destination reputation, asset criticality, and historical baselines.
