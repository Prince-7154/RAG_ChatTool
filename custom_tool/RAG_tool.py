from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field
from  tool_functions.rag_tool_function import rag_tool_function

class ragInput(BaseModel):
    query : str = Field(description="Input query for RAG tool")


rag_tool = StructuredTool.from_function(
    func = rag_tool_function,
    name = 'search_in_documents',
    description = "Use this tool to answer questions about the content of the uploaded documents.",
    args_schema = ragInput
)