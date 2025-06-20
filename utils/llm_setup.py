from langchain_together import ChatTogether
import os

def get_llm():
    llm = ChatTogether(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        temperature=0.2,
        together_api_key=os.getenv("OPENAI_API_KEY")
    )
    return llm
