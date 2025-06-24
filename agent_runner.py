from custom_tool.RAG_tool import rag_tool
from langchain.agents import create_tool_calling_agent,AgentExecutor
from utils.llm_setup import get_llm
from langchain.prompts import ChatPromptTemplate
from custom_tool.calender_tool import calendar_tool
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories.redis import RedisChatMessageHistory

tools = [rag_tool,calendar_tool]
llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a helpful assistant that answers user questions. "
        "Use the `rag_tool` to answer document-related queries, and the `calendar_tool` tool only if the user explicitly asks to create a calendar event.\n\n"
        "Only use information from tools. Do not fabricate answers.\n\n"
        "Examples:\n"
        "- If the user says 'Where does Prince Poudel lives?', use `rag_tool`.\n"
        "- If the user says 'Schedule a meeting titled Project Sync at today for 30 minutes', use calendar`."
        "- If the user says tommorrow, next day. Convert this format in correct date for Nepal calculated from today."
        ""
    )),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# Create chat memory using Redis
session_id = "user-session-1" 
chat_history = RedisChatMessageHistory(
    session_id="user-session-1",
    url="redis://default:kJn4i0xmw2N6Lw0ozqm4dLZk83XpFW9d@redis-15358.c283.us-east-1-4.ec2.redns.redis-cloud.com:15358",
    key_prefix="message_store:",
    ttl=3600,
)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    chat_memory=chat_history,
    return_messages=True
)


agent = create_tool_calling_agent(llm=llm, tools=tools,  prompt=prompt )

agent_executor = AgentExecutor(agent=agent,tools=tools,memory=memory, verbose=True)

def run_agent(input_text : str) -> str:
    response = agent_executor.invoke({"input": input_text})
    return response["output"] if isinstance(response, dict) else response


if __name__ == "__main__":
    
    while True:
        query = input("Ask me: ")
        if(query == "exit"):
            break
        response = run_agent(query)
        print([t.name for t in tools])
        print(response)
    

