from utils.pdf_chuncker import load_and_chunk
from utils.pinecone_db import pinecone_init, store_document
def pdf_loader(pdf_path:str, chunck_size: int = 500, chunk_overlap:int = 50):
    docs = load_and_chunk(pdf_path=pdf_path,chunk_size=chunck_size,chunk_overlap=chunk_overlap)
    pinecone_db = pinecone_init(index_name="rag-tool-index-new")
    store_document(pinecone_db,docs)

    return "PDF is loaded in rag-tool-index-new index at pinecone "