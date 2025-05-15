# 🚀 Estudo da API com FastAPI

## Introdução:
Este projeto é uma API REST simples feita com FastAPI em Python. 
O objetivo é aprender como criar, buscar, atualizar e deletar dados, 
além de entender como funciona a documentação automática da API e o tratamento de dados UTF-8.

## Requisitos
-  Python 3.7+;
-  FastAPI;
-  Uvicorn (servidor ASGI);

## Instalação:
```SH
pip install fastapi uvicorn
```
## Código Principal (app.py)
python
```Python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

dados = {
    1: {"nome": "Anderson", "idade": 35, "cidade": "São Paulo"},
    2: {"nome": "María", "idade": 28, "cidade": "Bogotá"},
    3: {"nome": "João", "idade": 42, "cidade": "Lisboa"}
}

class Pessoa(BaseModel):
    nome: str
    idade: int
    cidade: str

@app.get("/dados/{id}")
async def buscar_dados(id: int):
    item = dados.get(id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item não encontrado")

@app.post("/dados/")
async def criar_dado(pessoa: Pessoa):
    novo_id = max(dados.keys()) + 1 if dados else 1
    dados[novo_id] = pessoa.dict()
    return {"id": novo_id, **pessoa.dict()}

@app.put("/dados/{id}")
async def atualizar_dado(id: int, pessoa: Pessoa):
    if id in dados:
        dados[id] = pessoa.dict()
        return {"id": id, **pessoa.dict()}
    raise HTTPException(status_code=404, detail="Item não encontrado")

@app.delete("/dados/{id}")
async def deletar_dado(id: int):
    if id in dados:
        del dados[id]
        return {"detail": f"Item {id} deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Item não encontrado")
```
##  Executando a API
```
uvicorn app:app --reload
```

## Testando os Endpoints
-  GET /dados/{id}
Busca dados por ID
Retorna JSON com informações da pessoa
```
Exemplo: http://127.0.0.1:8000/dados/1
```

-  POST /dados/
Cria um novo registro
Recebe JSON no corpo da requisição com nome, idade e cidade
Exemplo JSON:
```
{
  "nome": "Lucas",
  "idade": 30,
  "cidade": "Curitiba"
}
```
-  PUT /dados/{id}
Atualiza dados de um ID existente
Recebe JSON igual ao POST

-  DELETE /dados/{id}
Deleta um registro pelo ID

## Documentação Automática
-  Acesse http://127.0.0.1:8000/docs para interface Swagger UI
-  Acesse http://127.0.0.1:8000/redoc para interface ReDoc


# 📦 API Simples de Itens com Flask (Projeto de Estudo)

Este é um projeto simples de API RESTful desenvolvido com Flask em Python. O objetivo principal é servir como material de estudo para entender os conceitos básicos de criação de APIs web, rotas, métodos HTTP, e manipulação de dados (neste caso, em memória).

## ✨ Funcionalidades

Esta API permite gerenciar uma lista de "itens" simples. As seguintes operações estão disponíveis:

* `GET /itens`: Lista todos os itens cadastrados.
* `GET /itens/<int:item_id>`: Retorna os detalhes de um item específico pelo seu ID.
* `POST /itens`: Adiciona um novo item à lista. Espera um corpo JSON com `name` e `descricao`.
* `PUT /itens/<int:item_id>`: Atualiza um item existente pelo seu ID. Espera um corpo JSON com os campos a serem atualizados (`name` e/ou `descricao`).
* `DELETE /itens/<int:item_id>`: Remove um item da lista pelo seu ID.

**Observação:** Os dados são armazenados apenas na memória e são perdidos toda vez que o servidor é reiniciado.

## 🚀 Tecnologias Utilizadas

* Python 3.x
* Flask: Microframework web para Python.
* Flask-CORS: Extensão para habilitar o CORS (Cross-Origin Resource Sharing), útil para testar com front-ends em outras portas/domínios.

## ⚙️ Como Configurar e Rodar

Siga os passos abaixo para colocar a API rodando na sua máquina local:

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/VenturaCerqueira/Python_backend_Educacional.git
    ```
2.  **Crie um Ambiente Virtual:**
    ```bash
    python -m venv venv
    ```

3.  **Ative o Ambiente Virtual:**
    * No Windows (Cmd): `venv\Scripts\activate`
    * No Windows (PowerShell): `venv\Scripts\Activate.ps1`
    * No Linux ou macOS: `source venv/bin/activate`

4.  **Instale as Dependências:**
    Com o ambiente virtual ativo, instale o Flask e o Flask-CORS:
    ```bash
    pip install Flask Flask-CORS
    ```

5.  **Execute a Aplicação Flask:**
    Na pasta do projeto (com o ambiente virtual ativo), rode o script:
    ```bash
    python app.py
    ```
    O servidor de desenvolvimento do Flask iniciará, geralmente em `http://127.0.0.1:5000/`.

## 🧪 Como Testar a API

Com o servidor rodando, você pode interagir com a API usando diversas ferramentas:

* **Navegador Web:** Para requisições `GET` simples (como `http://localhost:5000/itens` ou `http://localhost:5000/itens/1`).
* **cURL (Terminal):** Uma ferramenta de linha de comando.
* **Ferramentas Gráficas:** Postman, Insomnia, ou a extensão "REST Client" para VS Code. São ótimas para testar todos os tipos de requisições (GET, POST, PUT, DELETE) e trabalhar com corpos JSON.

**Exemplos de Requisições (usando cURL ou similar):**

* **GET todos os itens:**
    ```bash
    curl http://localhost:5000/itens
    ```

* **GET item específico (ex: ID 1):**
    ```bash
    curl http://localhost:5000/itens/1
    ```

* **POST novo item:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Tablet", "descricao": "Tablet Android 10"}' http://localhost:5000/itens
    ```

* **PUT atualizar item (ex: ID 1):**
    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"descricao": "Cadeira ergonômica nova"}' http://localhost:5000/itens/1
    ```

* **DELETE item (ex: ID 2):**
    ```bash
    curl -X DELETE http://localhost:5000/itens/2
    ```
