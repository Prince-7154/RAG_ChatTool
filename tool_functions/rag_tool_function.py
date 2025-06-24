from utils.pinecone_db import pinecone_init
from utils.llm_setup import get_llm
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap


def rag_tool_function(query: str) -> str:
    """
    Tool to call if query is about the Prince Poudel. Here it contains the resume of the prince.
    """

    vector_store = pinecone_init("rag-tool-index-new")
    retriever = vector_store.as_retriever()

    #  Retrieve relevant documents
    docs = retriever.invoke(query)

    #  Create context from document contents
    context = "\n\n".join(d.page_content for d in docs)

    llm = get_llm()

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "Answer using only the context below. "
            "If you can't find the answer, don’t add any new information.\n\n"
            "Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        )
    )

    chain = prompt | llm

    return chain.invoke({"context": context, "question": query})
