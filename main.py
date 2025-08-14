from dotenv import load_dotenv
import os
import asyncio
load_dotenv('.env')
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from notes_engine import notes_tool
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from pdf import metadata_engine

async def main():
    ordway_customer_path = os.path.join('data', 'customer.csv')
    ordway_custom_df = pd.read_csv(ordway_customer_path)

    ordway_query_engine = PandasQueryEngine(df=ordway_custom_df, verbose=True, instruction_str=instruction_str)
    ordway_query_engine.update_prompts({"pandas_prompt": new_prompt})

    tools = [
        notes_tool,
        QueryEngineTool(
            query_engine=ordway_query_engine,
            metadata=ToolMetadata(
                name="ordway_query_engine",
                description="Query engine for the Ordway customer data.",
            ),
        ),
        QueryEngineTool(
            query_engine=metadata_engine,
            metadata=ToolMetadata(
                name="metadata_query_engine",
                description="Query engine for the Ordway Metadata PDF.",
            ),
        )
    ]

    llm = OpenAI(
        model="gpt-4o",
        temperature=0.0,
    )

    agent = ReActAgent(llm=llm, tools=tools, verbose=True, context=context)

    while (prompt := input("Enter your query (or 'exit'): ")) != "exit":
        response = await agent.run(prompt)  # Using arun instead of run
        print(response)

if __name__ == "__main__":
    asyncio.run(main())