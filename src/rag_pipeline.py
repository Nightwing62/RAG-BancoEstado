import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma


DB_PATH = "db"


def crear_pipeline_rag(ruta_pdf):

    print("-> Preparando RAG...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    if os.path.exists(DB_PATH):

        print("-> Cargando ChromaDB existente...")

        vectorstore = Chroma(
            persist_directory=DB_PATH,
            embedding_function=embeddings
        )

    else:

        print("-> Leyendo PDF...")

        loader = PyPDFLoader(ruta_pdf)

        documentos = loader.load()

        print("-> Dividiendo documentos...")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(documentos)

        print("-> Creando ChromaDB...")

        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=DB_PATH
        )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever