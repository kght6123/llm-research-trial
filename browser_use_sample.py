from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

# task_prompt = "エリンギ、まいたけ、キャベツ、じゃがいも、とりむね肉、鶏もも肉、豚肉があります。この材料からいくつか使って、簡単な晩御飯のおかずを日本語で考えてください。3歳から6歳の子供が喜んで食べるものでお願いします。"
# task_prompt = "CSSの`@layer`ディレクティブについて、初心者向けに使い方とメリット、デメリットを教えてください。"
# task_prompt = "CSSの`@layer`ディレクティブについて、初心者向けに使い方をわかりやすいサンプルコード付きで教えてください。"
# task_prompt = "CSSの`color-mix`関数について、初心者向けに使い方とメリット、デメリットを教えてください。"
# task_prompt = "CSSの`color-mix`関数について、初心者向けに使い方をわかりやすいサンプルコード付きで教えてください。"
task_prompt = "CSSの`@property`ディレクティブについて、syntaxやinherits、initial-valueを使った場合のグラデーションのアニメートや大きなページでのパフォーマンス向上について、初心者向けに使い方をわかりやすいサンプルコード付きで教えてください。"

async def main():
    agent = Agent(
        task=task_prompt,
        llm=ChatOpenAI(model="gpt-4o-mini"),
    )
    await agent.run()

asyncio.run(main())