from config import OPENAI_API_KEY, GOOGLE_API_KEY, OPENAI_LLM_MODEL, GOOGLE_LLM_MODEL


def get_llm():
    """Retorna o modelo LLM baseado nas API keys disponíveis."""
    if OPENAI_API_KEY:
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=OPENAI_LLM_MODEL)
    elif GOOGLE_API_KEY:
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(model=GOOGLE_LLM_MODEL)
    else:
        raise ValueError("Nenhuma API key encontrada. Configure OPENAI_API_KEY ou GOOGLE_API_KEY no .env")
