# Desafio MBA Engenharia de Software com IA - Full Cycle

Sistema de ingestão e busca semântica em PDFs usando LangChain, PostgreSQL + pgVector.

## Pré-requisitos

- Python 3.10+
- Docker e Docker Compose

## Como executar

### 1. Subir o banco de dados

```bash
docker-compose up -d
```

Aguarde o container ficar saudável (a extensão pgVector será criada automaticamente).

### 2. Criar ambiente virtual e instalar dependências

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente

```bash
cp .env.example .env
```

Edite o arquivo `.env` e configure sua API key (OpenAI **ou** Google Gemini):

- **OpenAI**: preencha `OPENAI_API_KEY`
- **Gemini**: preencha `GOOGLE_API_KEY`

### 4. Ingestão do PDF

Coloque o arquivo PDF na raiz do projeto (ou ajuste `PDF_PATH` no `.env`) e execute:

```bash
python src/ingest.py
```

### 5. Chat via CLI

```bash
python src/chat.py
```

Exemplo de uso:

```
PERGUNTA: Qual o faturamento da Empresa SuperTechIABrazil?
RESPOSTA: O faturamento foi de 10 milhões de reais.

PERGUNTA: Qual é a capital da França?
RESPOSTA: Não tenho informações necessárias para responder sua pergunta.
```

Digite `sair` para encerrar o chat.

## Tecnologias

- Python + LangChain
- PostgreSQL + pgVector
- OpenAI ou Google Gemini (embeddings + LLM)
- Docker Compose
