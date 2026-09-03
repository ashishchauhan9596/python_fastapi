from fastapi import FastAPI, HTTPException
from app.services import fetch_competitive_news
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

@app.get("/")
def home():
    return {"message": "FastAPI is running"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/news")
async def api_fetch_fresh_news():
    # Call the common function
    result = await fetch_competitive_news()
    
    # If the service file returns an error, raise an HTTP 500
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
        
    # Otherwise, return the successful data
    return result