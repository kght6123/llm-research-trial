from gpt_researcher import GPTResearcher
from gpt_researcher.utils.enum import ReportType, Tone
import asyncio

async def main():
    # Initialize researcher with deep research type
    researcher = GPTResearcher(
        query="エリンギ、まいたけ、キャベツ、じゃがいも、とりむね肉、鶏もも肉、豚肉があります。この材料からいくつか使って、簡単な晩御飯のおかずを日本語で考えてください。3歳から6歳の子供が喜んで食べるものでお願いします。",
        report_type="deep",  # This triggers deep research modd
    )
    
    # Run research
    research_data = await researcher.conduct_research()
    
    # Generate report
    report = await researcher.write_report()
    print(report)

if __name__ == "__main__":
    asyncio.run(main())