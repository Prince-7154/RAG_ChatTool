from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from typing import List
import time
import os


def pinecone_init(index_name : str = "new_index", dimension: int = 384):

    pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

    if not pc.has_index(index_name):
        pc.create_index(
            name = index_name,
            dimension= dimension,
            metric = "cosine",
            spec=ServerlessSpec(cloud = "aws", region = "us-east-1")
        )
        while not pc.describe_index(index_name).status["ready"]:
            time.sleep(1)
        
    index = pc.Index(index_name)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = PineconeVectorStore(index = index, embedding=embeddings)

    return vector_store


def store_document( vector_store : PineconeVectorStore ,docs : List[Document]):

    """
    Stores the data in the pinecone database by embedding the document.
    """

    ids = [f"Docs_{i}" for i in range(len(docs))]
    inserted_docs = vector_store.add_documents(documents=docs, ids = ids)

    print(f"Inserted {len(inserted_docs)} documents")








