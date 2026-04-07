from search import search_and_answer


def main():
    print("Chat RAG - Faça perguntas sobre o PDF")
    print("Digite 'sair' para encerrar.\n")

    while True:
        question = input("PERGUNTA: ").strip()

        if not question:
            continue

        if question.lower() == "sair":
            print("Encerrando chat. Até logo!")
            break

        try:
            answer = search_and_answer(question)
            print(f"RESPOSTA: {answer}\n")
        except Exception as e:
            print(f"Erro ao processar pergunta: {e}\n")


if __name__ == "__main__":
    main()
