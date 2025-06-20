from custom_tool.RAG_tool import rag_tool
from langchain.agents import create_tool_calling_agent,AgentExecutor
from utils.llm_setup import get_llm
from langchain.prompts import ChatPromptTemplate

tools = [rag_tool]
llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system", "Use rag tool to search in documets. donot modify the output of rag tool and do not add your own information. If you can't find the answer, just say 'I don't know. '"),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# prompt = PromptTemplate(
#         input_variables=["context", "question"],
#         template=(
#             "Answer using only the context below. "
#             "If you can't find the answer, say 'I don't know.'\n\n"
#             "Context:\n{context}\n\nQuestion: {question}\nAnswer:"
#         )   
#     )

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt )

agent_executor = AgentExecutor(agent=agent,tools=tools, verbose=True)

def run_agent(input_text : str) -> str:
    response = agent_executor.invoke({"input": input_text})
    return response["output"] if isinstance(response, dict) else response


if __name__ == "__main__":
    query = input("Ask me: ")
    response = run_agent(query)
    print(response)
    

