import logging
import os

from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://postgres:postgres@localhost:5432/rag")
COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME", "pdf_chunks")
PDF_PATH = os.getenv("PDF_PATH", "document.pdf")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
GOOGLE_EMBEDDING_MODEL = os.getenv("GOOGLE_EMBEDDING_MODEL", "models/embedding-001")

OPENAI_LLM_MODEL = os.getenv("OPENAI_LLM_MODEL", "gpt-5-nano")
GOOGLE_LLM_MODEL = os.getenv("GOOGLE_LLM_MODEL", "gemini-2.5-flash-lite")
