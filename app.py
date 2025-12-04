from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent 
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()

api_key =os.getenv("GOOGLE_API_KEY")

async def main():
    agent=Agent(
        task="Go to youtube and search 'Agentic AI' and provide me the playlist on the topic Agentic AI",
        llm=ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            api_key=api_key
        )
    )
    result=await agent.run()
    print(result)
    
asyncio.run(main())


