from utils.pinecone_db import pinecone_init
from utils.llm_setup import get_llm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def rag_tool_function(query: str) -> str:

    """
    Tool to call if query is about the Prince Poudel. Here it contain the resume of the prince.
    """

    vector_store = pinecone_init("rag-tool-index-new")
    retriver = vector_store.as_retriever()

    llm = get_llm()

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "Answer using only the context below. "
            "If you can't find the answer, say 'I don't know.'\n\n"
            "Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        )   
    )

    chain = LLMChain(llm = llm, prompt = prompt)

    docs = retriver.get_relevant_documents(query=query)

    context = "\n\n".join(d.page_content for d in docs)

    return chain.run(context = context, question = query)





    