# Module 09.7 — Docker for AI Services

## Capability
Package runtime dependencies into reproducible containers.

## Core model
Images capture filesystem/runtime dependencies; containers isolate process execution but not external data/config/secrets.

## Practice
Build minimal image and run service with mounted/configured environment.

## Debug / transfer
Fix huge image, missing model artifact or secret baked into image.

## Evidence to save
Dockerfile + .dockerignore + documented run command.

## Mastery
Container starts from clean host assumptions.
