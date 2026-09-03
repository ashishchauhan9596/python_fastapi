import os
from langchain_google_genai import ChatGoogleGenerativeAI

async def fetch_competitive_news():
    """Common function to fetch news using Gemini Google Search."""
    if not os.getenv("GOOGLE_API_KEY"):
        return {"error": "Missing GOOGLE_API_KEY environment variable."}
        
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        temperature=0.2,
        max_retries=2
    )
    
    prompt = """
    You are an expert tutor for Indian competitive exams, specializing in both Central government exams (UPSC, SSC) and Himachal Pradesh state exams (HPAS, HPRCA, Allied Services, Panchayat Secretary).
    
    Using Google Search, fetch the absolute latest, breaking current affairs from TODAY. 
    You must divide the news into TWO distinct sections:
    
    ### Section 1: National & International Affairs (Central Exams)
    Focus on major geopolitical events, Supreme Court rulings, national economic policies, and defense.
    
    ### Section 2: Himachal Pradesh Specific Affairs (State Exams)
    Focus on HP state government decisions, regional infrastructure projects, state environmental news, and local administration updates.
    
    For every news item in both sections, strictly format it as a Markdown list containing:
    - **Headline**: 
    - **Date**: 
    - **Core Facts**: (2-3 crisp bullet points of what happened)
    - **Exam Relevance**: (Briefly explain how this could be asked in a Central or HP state exam)
    """
    
    try:
        response = await llm.ainvoke(prompt, tools=[{"google_search": {}}])
        return {"status": "success", "data": response.content}
    except Exception as e:
        return {"error": f"Failed to fetch news: {str(e)}"}