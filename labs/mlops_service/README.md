# MLOps Service Lab

`service.py` exposes a tiny deterministic prediction service with `/health` and `/predict`. It is deliberately framework-light so packaging and operational behavior remain visible.

Tasks:

- run and test it locally,
- containerize it with the provided Dockerfile,
- add request validation and structured logging,
- add model/version metadata,
- inject malformed requests and restart the service,
- write a rollback/runbook note.

The point is production engineering behavior, not model complexity.
