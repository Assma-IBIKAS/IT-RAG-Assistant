from langchain_chroma import Chroma
from embeddings import create_vectorstore

def get_retriever(persist_directory: str,create_vectorstore,k: int = 3):

    # Crée et retourne un retriever à partir d'une Vector DB Chroma

    # Charger la base vectorielle existante
    vectorstore = Chroma(
        persist_directory = persist_directory,
        embedding_function = create_vectorstore
    )

    # Créer le retriever
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k}
    )

    return retriever  