from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# fonction d'embeddings + stocker dans chroma_db
def create_vectorstore(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
    )
    persist_directory = "./chroma_db"
    vectorstore = Chroma.from_documents(
        documents = chunks,
        embedding = embeddings,
        persist_directory = persist_directory
    )

    db_data = vectorstore.get(include = ['documents','embeddings','metadatas'])

    print("=====================================================================")
    print(f"Number of stored chunks : {len(db_data['documents'])}")
    print("=====================================================================")
    
    return db_data 