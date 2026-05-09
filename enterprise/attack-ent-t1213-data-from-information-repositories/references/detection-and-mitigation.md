# Detection and Mitigation Notes

## Technique

- ATT&CK ID: T1213
- Name: Data from Information Repositories
- Domain: enterprise
- Tactics: collection
- Platforms: Linux, Windows, macOS, SaaS, IaaS, Office Suite

## ATT&CK detection guidance

No ATT&CK detection guidance was present in the source STIX object.

## Telemetry checklist

- Not specified in the STIX object.

## Mitigation candidates

- Audit
- Encrypt Sensitive Information
- Multi-factor Authentication
- Out-of-Band Communications Channel
- Software Configuration
- User Account Management
- User Training

## Triage questions

- What asset, identity, workload, application, or control-plane component is in scope?
- Which observed events directly align with the ATT&CK behavior, and which are only circumstantial?
- What telemetry is missing, delayed, filtered, or known to be unreliable?
- Is this a single event, repeated pattern, campaign-level behavior, or expected administrative activity?
- What compensating controls should have prevented, detected, or limited the behavior?

## False-positive considerations

- Authorized administration, software deployment, security tooling, backup activity, and automated platform maintenance can resemble ATT&CK behavior.
- Before escalating, compare command lineage, account ownership, change tickets, destination reputation, asset criticality, and historical baselines.
