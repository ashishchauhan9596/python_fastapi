import asyncio
from datetime import datetime
from app.services import fetch_competitive_news

async def fetch_news_job():
    """Runs the heavy news fetcher every day at 8:00 AM."""
    while True:
        now = datetime.now()
        
        if now.hour == 8 and now.minute == 0:
            print(f"[{datetime.now()}] Triggering daily news fetcher...")
            
            # Call the common function
            result = await fetch_competitive_news()
            
            if "error" in result:
                print(f"Error: {result['error']}")
            else:
                print("\n=== DAILY NEWS FETCHED SUCCESSFULLY ===")
                print(result["data"])
                
            # Sleep 61 seconds so it doesn't trigger twice at 8:00
            await asyncio.sleep(61)
        else:
            # Check the time every 30 seconds
            await asyncio.sleep(30)

async def five_minute_job():
    """Runs a simple timer exactly every 5 minutes."""
    while True:
        print(f"[{datetime.now()}] 5-Minute Timer Executed.")
        # Sleep for 300 seconds (5 minutes) before running again
        await asyncio.sleep(300)

async def main():
    print(f"Starting custom Python native scheduler at {datetime.now()}...")
    
    # asyncio.gather runs both of your infinite loops concurrently alongside each other
    await asyncio.gather(
        fetch_news_job(),
        five_minute_job()
    )

if __name__ == "__main__":
    # Start the asyncio event loop and run the main coroutine
    asyncio.run(main())