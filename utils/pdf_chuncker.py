
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document

def load_and_chunk(pdf_path: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Document]:
    """
    Loads a PDF file, splits pages into text chunks (Documents), and returns them.
    """
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    docs = splitter.split_documents(pages)
    return docs


