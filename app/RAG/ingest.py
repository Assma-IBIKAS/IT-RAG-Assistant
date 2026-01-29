from langchain_community.document_loaders import PyPDFLoader

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