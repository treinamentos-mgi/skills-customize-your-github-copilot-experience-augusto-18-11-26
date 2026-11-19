# 📘 Atividade: Testing APIs with FastAPI and pytest

## 🎯 Objetivo

Escreva testes automatizados para uma API FastAPI usando pytest e `TestClient`. Você vai verificar respostas de sucesso, criação de dados e tratamento de erros HTTP.

## 📝 Tarefas

### 🛠️ Executar e Explorar os Testes Iniciais

#### Descrição
Instale as dependências e execute os dois testes de exemplo. Leia `app.py` e `test_api.py` para identificar como o `TestClient` faz requisições sem iniciar um servidor e como a fixture reinicia os dados antes de cada teste.

```bash
python -m pip install fastapi pytest httpx2
cd assignments/testing-fastapi-apis
python -m pytest -q
```

#### Requisitos
O programa concluído deve:

- Executar os testes de exemplo sem iniciar o servidor Uvicorn
- Manter cada teste independente usando a fixture `client`
- Adicionar um teste para `GET /tasks/999` que confirme o status HTTP 404


### 🛠️ Testar a Criação de uma Tarefa

#### Descrição
Escreva um teste para criar uma tarefa com `POST /tasks`. Envie um título e verifique a resposta e a tarefa retornada.

#### Requisitos
O programa concluído deve:

- Confirmar que `POST /tasks` retorna status HTTP 201
- Confirmar que a resposta contém um ID, o título enviado e `completed` como `false` quando esse campo não é enviado
- Confirmar que a tarefa criada aparece em `GET /tasks`


### 🛠️ Verificar Entradas Inválidas

#### Descrição
Envie uma requisição de criação sem título e outra com título vazio. Verifique como a API valida os dados antes de criar a tarefa.

#### Requisitos
O programa concluído deve:

- Confirmar que uma requisição sem o campo `title` retorna status HTTP 422
- Confirmar que um título vazio retorna status HTTP 422
- Confirmar que uma requisição inválida não adiciona uma tarefa à lista
- Executar toda a suíte com `python -m pytest -q` e observar todos os testes aprovados