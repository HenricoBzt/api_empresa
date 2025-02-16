# API Empresa

Esta é uma API para gerenciamento de empresas e obrigações acessórias, desenvolvida com FastAPI, SQLAlchemy, Pydantic e testes com pytest.

## Tecnologias Utilizadas
- Python (FastAPI)
- SQLAlchemy com Alembic
- Pydantic
- PostgreSQL (para produção) e SQLite (para testes)
- Pytest

## Como Rodar o Projeto

### Pré-requisitos
- Python 3.9+
- PostgreSQL (ou utilizar SQLite para testes)

### Configuração
1. Clone o repositório:
   git clone https://github.com/seu_usuario/api_empresa.git

2. Crie e ative o ambiente virtual

3. Instale as dependências:
pip install -r requirements.txt

4. Crie um arquivo .env copiando o .env.example e configure as variáveis de ambiente:
cp .env.example .env

5. Rode a aplicação:
uvicorn crud:app --reload

6. Acesse a documentação no Swagger UI em http://127.0.0.1:8000/docs.


7. Para rodar os testes, utilize:
pytest


---

## **3. Inicialize o Repositório Git e Faça o Primeiro Commit**

Abra o terminal na pasta do projeto e execute os comandos abaixo:

1. **Inicialize o repositório Git:**
   git init