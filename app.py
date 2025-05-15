
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# Dados para buscar 
dados = {
    1: {"nome": "Anderson", "idade": 35, "cidade": "São Paulo"},
    2: {"nome": "María", "idade": 28, "cidade": "Bogotá"},
    3: {"nome": "João", "idade": 42, "cidade": "Lisboa"}
}

# Modelo para validar os dados de entrada:
class Pessoa(BaseModel):
    nome: str
    idade: int
    cidade: str
    # Adiciona o campo 'id' para identificar a pessoa


# Buscar dados pelo ID (GET)
@app.get("/dados/{id}")
async def buscar_dados(id: int):
    """
    Busca dados pelo ID.
    """
    item = dados.get(id)
    if item:
        return JSONResponse(content=item) # Retorna os dados encontrados
    return JSONResponse(status_code=404, content={"message": "Item não encontrado"}) # Retorna erro 404 se não encontrar

# Criar novo dados (POST)
@app.post("/dados/")
async def criar_dados(pessoa: Pessoa):
    """
    Cria um novo dado.
    """
    novo_id = max(dados.keys()) + 1 if dados else 1
    dados[novo_id] = pessoa.dict()
    return {"id": novo_id, **pessoa.dict()} # Retorna o ID do novo dado criado

# Atualizar dados (PUT)
@app.put("/dados/{id}")
async def atualizar_dados(id: int, pessoa: Pessoa):
    """
    Atualiza um dado existente.
    """
    if id in dados:
        dados[id] = pessoa.dict()
        return {"id": id, **pessoa.dict()}
    raise HTTPException(status_code=404, detail="Item não encontrado") # Retorna erro 404 se não encontrar

# Deletar dados (Delete)
@app.delete("/dados/{id}")
async def deletar_dados(id: int):
    """
    Deleta um dado existente.
    """
    if id in dados:
        del dados[id]
        return {"detail": f"Item {id} deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Item não encontrado")

