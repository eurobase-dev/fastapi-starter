# FastAPI starter for Eurobase

A minimal FastAPI app with `/` and `/health`. Ready to deploy on [Eurobase](https://eurobase.dev), a cloud for deploying web apps from GitHub, made in Europe.

## Deploy

1. Select **Use this template** to create your own copy of this repository.
2. In [Eurobase](https://eurobase.dev), create a project from your copy. Eurobase detects FastAPI, builds a container and starts it with `uvicorn`. No Dockerfile is needed.
3. Every push to `main` deploys again. You can roll back to any earlier deployment.

### With a coding agent

Connect Claude Code, Codex, Cursor, Zed or VS Code to Eurobase ([how](https://eurobase.dev/docs/agents)), then ask your agent:

> Deploy this project on Eurobase.

## Run it locally

```sh
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Learn more

- [Getting started](https://eurobase.dev/docs/getting-started)
- [Deploy a FastAPI app: step-by-step guide](https://eurobase.dev/docs/guides/fastapi)
- [How FastAPI runs on Eurobase (containers)](https://eurobase.dev/docs/containers)
- [Plans and limits](https://eurobase.dev/docs/plans): the Free plan costs nothing.
