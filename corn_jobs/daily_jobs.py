from datetime import datetime
import asyncio

async def run_job():
    print(f"Corn job execute at {datetime.now()}")

if __name__ == "__main__":
    asyncio.run(run_job())