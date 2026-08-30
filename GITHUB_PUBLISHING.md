# GitHub Publishing Guide

This directory is designed to be a normal Git repository. Keep the GitHub repository private while you are still changing personal notes or experimenting; make it public only when you are comfortable sharing the curriculum.

## Local-first workflow
1. Edit/audit locally.
2. Commit meaningful checkpoints.
3. Create an empty GitHub repository named for this academy.
4. Add it as `origin`.
5. Push `main` and release tags.

Typical commands after the GitHub repository exists:

```bash
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
git push origin --tags
```

## Important
- Never commit API keys, tokens, credentials, private learner data, paid copyrighted course files, or client information.
- External resources are linked/referenced; do not copy proprietary course content into this repository.
- Before a public release, follow `PUBLISHING_CHECKLIST.md` and update fast-moving resources/market notes.

This v1.0 package is local-first; it does not require GitHub to study from it.
