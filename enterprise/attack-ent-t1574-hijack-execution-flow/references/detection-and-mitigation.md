# Detection and Mitigation Notes

## Technique

- ATT&CK ID: T1574
- Name: Hijack Execution Flow
- Domain: enterprise
- Tactics: execution, stealth
- Platforms: Linux, macOS, Windows

## ATT&CK detection guidance

No ATT&CK detection guidance was present in the source STIX object.

## Telemetry checklist

- Not specified in the STIX object.

## Mitigation candidates

- Application Developer Guidance
- Audit
- Behavior Prevention on Endpoint
- Execution Prevention
- Restrict File and Directory Permissions
- Restrict Library Loading
- Restrict Registry Permissions
- Update Software
- User Account Control
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
