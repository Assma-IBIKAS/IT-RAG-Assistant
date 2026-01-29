from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# path de pdf 
pdf_path = "../../data/pdf_data.pdf"

# fonction pour loader data_pdf
def load_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    print("=====================================================================")
    print(docs[0].page_content)
    print("=---------------------------------------------------------------------=")
    print(f"len de document : {len(docs)}")
    print("=---------------------------------------------------------------------=")
    print(docs[0].metadata)
    print("=====================================================================")
    return docs 

# fonction pour splitter le document (chunks)
def split_pdf(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 80
    )

    chunks = splitter.split_documents(docs)

    print("=====================================================================")
    print(f"len de chunks : {len(chunks)}")
    print("=====================================================================")

    return chunks