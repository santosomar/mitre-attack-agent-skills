# Detection and Mitigation Notes

## Technique

- ATT&CK ID: T1098
- Name: Account Manipulation
- Domain: enterprise
- Tactics: persistence, privilege-escalation
- Platforms: Containers, ESXi, IaaS, Identity Provider, Linux, macOS, Network Devices, Office Suite, SaaS, Windows

## ATT&CK detection guidance

No ATT&CK detection guidance was present in the source STIX object.

## Telemetry checklist

- Not specified in the STIX object.

## Mitigation candidates

- Disable or Remove Feature or Program
- Multi-factor Authentication
- Network Segmentation
- Operating System Configuration
- Privileged Account Management
- Restrict File and Directory Permissions
- User Account Management

## Triage questions

- What asset, identity, workload, application, or control-plane component is in scope?
- Which observed events directly align with the ATT&CK behavior, and which are only circumstantial?
- What telemetry is missing, delayed, filtered, or known to be unreliable?
- Is this a single event, repeated pattern, campaign-level behavior, or expected administrative activity?
- What compensating controls should have prevented, detected, or limited the behavior?

## False-positive considerations

- Authorized administration, software deployment, security tooling, backup activity, and automated platform maintenance can resemble ATT&CK behavior.
- Before escalating, compare command lineage, account ownership, change tickets, destination reputation, asset criticality, and historical baselines.
