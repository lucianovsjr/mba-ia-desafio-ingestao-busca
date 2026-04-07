from embeddings import get_vector_store
from llm import get_llm
from prompts import PROMPT_TEMPLATE


def search_and_answer(question: str) -> str:
    """Busca contexto relevante no banco vetorial e gera resposta via LLM."""
    vector_store = get_vector_store()
    results = vector_store.similarity_search_with_score(question, k=10)

    contexto = "\n\n".join([doc.page_content for doc, _score in results])

    prompt = PROMPT_TEMPLATE.format(contexto=contexto, pergunta=question)

    llm = get_llm()
    response = llm.invoke(prompt)

    return response.content
