# Desafio MBA Engenharia de Software com IA - Full Cycle

Sistema de Retrieval-Augmented Generation (RAG) para perguntas e respostas sobre documentos PDF, usando LangChain, PostgreSQL + pgVector e modelos da OpenAI ou Google Gemini.

## Arquitetura

```
PDF → Ingestão (chunks + embeddings) → PostgreSQL/pgVector
                                              ↓
Pergunta do usuário → Busca semântica → Contexto → LLM → Resposta
```

### Estrutura do projeto

```
├── src/
│   ├── config.py        # Variáveis de ambiente e configurações
│   ├── embeddings.py    # Seleção do modelo de embeddings (OpenAI / Gemini)
│   ├── ingest.py        # Carregamento e ingestão do PDF no banco vetorial
│   ├── search.py        # Busca semântica + geração de resposta via LLM
│   └── chat.py          # Interface CLI de chat
├── docker-compose.yml   # PostgreSQL + pgVector
├── requirements.txt     # Dependências Python
├── .env.example         # Template de variáveis de ambiente
└── document.pdf         # PDF para ingestão (exemplo)
```

## Pré-requisitos

- Python 3.10+
- Docker e Docker Compose

## Como executar

### 1. Subir o banco de dados

```bash
docker-compose up -d
```

Aguarde o container ficar saudável — a extensão pgVector será criada automaticamente pelo serviço `bootstrap_vector_ext`.

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

Edite o `.env` e configure a API key do provedor desejado:

| Variável | Descrição | Padrão |
|---|---|---|
| `OPENAI_API_KEY` | Chave da API OpenAI | — |
| `GOOGLE_API_KEY` | Chave da API Google Gemini | — |
| `OPENAI_EMBEDDING_MODEL` | Modelo de embeddings OpenAI | `text-embedding-3-small` |
| `GOOGLE_EMBEDDING_MODEL` | Modelo de embeddings Gemini | `models/embedding-001` |
| `OPENAI_LLM_MODEL` | Modelo LLM OpenAI | `gpt-5-nano` |
| `GOOGLE_LLM_MODEL` | Modelo LLM Gemini | `gemini-2.5-flash-lite` |
| `DATABASE_URL` | URL de conexão PostgreSQL | `postgresql+psycopg://postgres:postgres@localhost:5432/rag` |
| `PG_VECTOR_COLLECTION_NAME` | Nome da coleção no pgVector | `pdf_chunks` |
| `PDF_PATH` | Caminho do PDF para ingestão | `document.pdf` |

> Basta configurar **uma** das chaves (`OPENAI_API_KEY` ou `GOOGLE_API_KEY`). O sistema detecta automaticamente qual provedor usar.

### 4. Ingestão do PDF

Coloque o arquivo PDF na raiz do projeto (ou ajuste `PDF_PATH` no `.env`) e execute:

```bash
python src/ingest.py
```

O processo carrega o PDF, divide em chunks de 1000 caracteres (com overlap de 150), gera embeddings e armazena no PostgreSQL via pgVector.

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

O modelo responde **somente** com base no conteúdo do PDF. Perguntas fora do contexto do documento são recusadas. Digite `sair` para encerrar.

## Tecnologias

- **LangChain** — orquestração de RAG (loaders, splitters, vector stores, LLMs)
- **PostgreSQL + pgVector** — armazenamento vetorial para busca por similaridade
- **OpenAI** ou **Google Gemini** — embeddings e geração de texto (LLM)
- **Docker Compose** — infraestrutura local do banco de dados
