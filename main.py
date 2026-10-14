from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="FastAPI starter for Eurobase")


@app.get("/")
def read_root():
    return {"message": "Hello from Eurobase"}


@app.get("/health")
def health():
    return {"status": "ok", "time": datetime.now(timezone.utc).isoformat()}
