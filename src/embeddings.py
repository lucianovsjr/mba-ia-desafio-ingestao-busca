from config import OPENAI_API_KEY, GOOGLE_API_KEY, OPENAI_EMBEDDING_MODEL, GOOGLE_EMBEDDING_MODEL


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
