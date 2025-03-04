from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="エリンギ、まいたけ、キャベツ、じゃがいも、とりむね肉、鶏もも肉、豚肉があります。この材料からいくつか使って、簡単な晩御飯のおかずを日本語で考えてください。3歳から6歳の子供が喜んで食べるものでお願いします。",
        llm=ChatOpenAI(model="gpt-4o-mini"),
    )
    await agent.run()

asyncio.run(main())