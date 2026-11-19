# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI. Você vai praticar rotas HTTP, operações CRUD, validação de dados e respostas de erro.

## 📝 Tarefas

### 🛠️ Criar Rotas para Consultar Tarefas

#### Descrição
Instale FastAPI e Uvicorn, execute o código inicial e complete as rotas para consultar tarefas. A rota `GET /tasks` já está pronta; adicione uma rota para consultar uma tarefa pelo ID.

Para instalar as dependências e iniciar a API:

```bash
python -m pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

Abra `http://127.0.0.1:8000/docs` para explorar e testar as rotas interativamente.

#### Requisitos
O programa concluído deve:

- Retornar a lista de tarefas em `GET /tasks` com status HTTP 200
- Implementar `GET /tasks/{task_id}` para retornar a tarefa com o ID solicitado
- Retornar status HTTP 404 quando o ID solicitado não existir


### 🛠️ Implementar Criação e Remoção

#### Descrição
Expanda a API para permitir criar tarefas e removê-las. Cada tarefa deve receber um ID numérico único durante a execução do servidor.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para criar uma tarefa com título e estado de conclusão
- Retornar a tarefa criada com status HTTP 201 e seu novo ID
- Implementar `DELETE /tasks/{task_id}` e retornar status HTTP 204 ao remover uma tarefa existente
- Retornar status HTTP 404 ao tentar remover uma tarefa inexistente


### 🛠️ Atualizar Tarefas com Validação

#### Descrição
Adicione uma rota para atualizar parcialmente uma tarefa existente. Valide os dados recebidos com modelos do Pydantic e teste tanto entradas válidas quanto inválidas na página `/docs`.

#### Requisitos
O programa concluído deve:

- Implementar `PATCH /tasks/{task_id}` para atualizar o título, o estado de conclusão ou ambos
- Rejeitar títulos vazios e retornar status HTTP 422 para dados inválidos
- Retornar status HTTP 404 quando a tarefa a atualizar não existir
- Preservar os campos que não forem enviados na atualização