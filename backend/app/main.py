from fastapi import FastAPI

app = FastAPI(title="Personal AI Memory OS")

@app.get("/health")
async def health():
    return {"status": "running"}