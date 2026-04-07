import logging

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import PDF_PATH
from embeddings import get_vector_store

logger = logging.getLogger(__name__)


def ingest_pdf():
    logger.info(f"Carregando PDF: {PDF_PATH}")
    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()
    logger.info(f"Páginas carregadas: {len(documents)}")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(documents)
    logger.info(f"Chunks gerados: {len(chunks)}")

    vector_store = get_vector_store()

    vector_store.add_documents(chunks)
    logger.info("Ingestão concluída com sucesso!")


if __name__ == "__main__":
    ingest_pdf()
