# Module 08.6 — Human-in-the-Loop Approval

## Capability
Insert human decisions at consequential/ambiguous boundaries.

## Core model
Approval is an architectural control: preview action/context, capture decision, resume safely and prevent duplicate side effects.

## Practice
Design approval for sending external messages or changing records.

## Debug / transfer
Handle timeout/rejection/restart after approval.

## Evidence to save
Approval state machine and tests.

## Mastery
System never treats silence as permission.
