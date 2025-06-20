from utils.pdf_chuncker import load_and_chunk
from utils.pinecone_db import pinecone_init, store_document


def main():
    docs = load_and_chunk("pdf\Resume-Prince-Poudel.pdf",500,50)
    pinecone_db = pinecone_init(index_name="rag-tool-index-new")
    store_document(pinecone_db,docs)



if __name__ == "__main__":
    
    main()