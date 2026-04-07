from langchain_postgres import PGVector
from config import DATABASE_URL, COLLECTION_NAME, OPENAI_LLM_MODEL, GOOGLE_LLM_MODEL, OPENAI_API_KEY, GOOGLE_API_KEY
from embeddings import get_embeddings


PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""


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


def get_vector_store():
    """Retorna o vector store conectado ao PostgreSQL."""
    embeddings = get_embeddings()
    return PGVector(
        embeddings=embeddings,
        collection_name=COLLECTION_NAME,
        connection=DATABASE_URL,
        use_jsonb=True,
    )


def search_and_answer(question: str) -> str:
    """Busca contexto relevante no banco vetorial e gera resposta via LLM."""
    vector_store = get_vector_store()
    results = vector_store.similarity_search_with_score(question, k=10)

    contexto = "\n\n".join([doc.page_content for doc, _score in results])

    prompt = PROMPT_TEMPLATE.format(contexto=contexto, pergunta=question)

    llm = get_llm()
    response = llm.invoke(prompt)

    return response.content
