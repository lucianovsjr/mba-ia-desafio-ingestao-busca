from langchain_postgres import PGVector
from config import (
    OPENAI_API_KEY, GOOGLE_API_KEY,
    OPENAI_EMBEDDING_MODEL, GOOGLE_EMBEDDING_MODEL,
    DATABASE_URL, COLLECTION_NAME,
)


def get_embeddings():
    """Retorna o modelo de embeddings baseado nas API keys disponíveis."""
    if OPENAI_API_KEY:
        from langchain_openai import OpenAIEmbeddings
        return OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL)
    elif GOOGLE_API_KEY:
        from langchain_google_genai import GoogleGenerativeAIEmbeddings
        return GoogleGenerativeAIEmbeddings(model=GOOGLE_EMBEDDING_MODEL)
    else:
        raise ValueError(
            "Nenhuma API key encontrada. Configure OPENAI_API_KEY ou GOOGLE_API_KEY no .env"
        )


def get_vector_store():
    """Retorna o vector store conectado ao PostgreSQL."""
    embeddings = get_embeddings()
    return PGVector(
        embeddings=embeddings,
        collection_name=COLLECTION_NAME,
        connection=DATABASE_URL,
        use_jsonb=True,
    )
