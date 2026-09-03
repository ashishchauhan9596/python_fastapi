from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is running"}


@app.get("/health")
def health():
    return {"status": "ok"}