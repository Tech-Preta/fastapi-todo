# Lista de Tarefas API

Este projeto é uma API simples para gerenciar uma lista de tarefas usando FastAPI e Python.

## Funcionalidades

GET /tasks: Lista todas as tarefas ou filtra tarefas por status de conclusão.
POST /tasks: Cria uma nova tarefa.
PUT /tasks/{task_id}: Atualiza uma tarefa existente.
DELETE /tasks/{task_id}: Remove uma tarefa.

## Tecnologias Utilizadas

- FastAPI
- Pydantic
- Uvicorn

## Como Executar

Siga os passos abaixo para executar o projeto localmente.

### Pré-requisitos

Certifique-se de ter Python 3.6+ instalado em sua máquina.

### Instalação

Primeiro, clone o repositório para a sua máquina local:


git clone https://github.com/Tech-Preta/fastapi-todo.git


Em seguida, instale as dependências necessárias:


pip install fastapi uvicorn


### Execução

Para iniciar o servidor, execute o seguinte comando no diretório do projeto:


uvicorn main:app --reload


O servidor estará rodando em http://127.0.0.1:8000.

## Documentação

Após executar o projeto, você pode acessar a documentação interativa gerada pelo FastAPI em http://127.0.0.1:8000/docs.