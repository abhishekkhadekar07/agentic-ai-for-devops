from langchain_mcp_adapters.client import MultiServerMCPClient 
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
import asyncio

async def main():
    # this brings all the tools from mcp server

    client = MultiServerMCPClient(
        {
            "docker-mcp": {
                "transport": "stdio",  # Local subprocess communication
                "command": "python",
                # Absolute path to your math_server.py file
                "args": ["mcp_server.py"],
                          },
        }
)
  
    tools = await client.get_tools();
    model = ChatOllama(model="gpt-oss:120b-cloud",temperature="0.8") #LLM
    # agent with mcp tools
    agent = create_agent(
        model,
        tools  
    )
    
    responce = await agent.ainvoke({"messages" : [{'role': 'user','content':"How many container are runnings"}]})
    print(responce['messages'][-1].content)

if __name__ == "__main__":
    asyncio.run(main())