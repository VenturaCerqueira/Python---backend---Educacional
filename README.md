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
