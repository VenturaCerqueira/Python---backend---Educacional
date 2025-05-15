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


# 2. 📦 API Simples de Itens com Flask (Projeto de Estudo)
## itens.py
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
    
# 3. 📦 API de Gerenciamento de Itens com Flask e SQLAlchemy (Projeto de Estudo)
## consultaBanco.py

Este projeto é uma evolução da API simples de itens. Agora, ele utiliza o framework Flask em conjunto com a extensão **Flask-SQLAlchemy** e um banco de dados **SQLite** para persistir os dados, em vez de armazená-los apenas na memória.

O objetivo continua sendo servir como material de estudo, focando em:

* Criação de APIs RESTful com Flask.
* Utilização de um ORM (SQLAlchemy) para interagir com o banco de dados usando objetos Python.
* Configuração e uso básico do Flask-SQLAlchemy.
* Persistência de dados em um banco SQLite.

## ✨ Funcionalidades

A API oferece os seguintes endpoints para gerenciar os itens no banco de dados:

* `GET /itens`: Lista todos os itens cadastrados no banco de dados.
* `GET /itens/<int:item_id>`: Retorna os detalhes de um item específico pelo seu ID.
* `POST /itens`: Adiciona um novo item ao banco de dados. Espera um corpo JSON com `name` e `descricao`.
* `PUT /itens/<int:item_id>`: Atualiza um item existente pelo seu ID no banco de dados. Espera um corpo JSON com os campos a serem atualizados (`name` e/ou `descricao`).
* `DELETE /itens/<int:item_id>`: Remove um item do banco de dados pelo seu ID.

## 🚀 Tecnologias Utilizadas

* Python 3.x
* Flask: Microframework web.
* Flask-SQLAlchemy: Extensão para integrar SQLAlchemy ao Flask.
* SQLAlchemy: ORM (Object-Relational Mapper).
* SQLite: Banco de dados leve baseado em arquivo.
* Flask-CORS: Extensão para habilitar o CORS.

## ⚙️ Como Configurar e Rodar

Siga os passos abaixo para configurar e executar a API:

1.  **Crie e Ative um Ambiente Virtual:**
    É crucial usar um ambiente virtual.
    ```bash
    python -m venv venv
    ```
    Ative o ambiente:
    * No Windows (Cmd): `venv\Scripts\activate`
    * No Windows (PowerShell): `venv\Scripts\Activate.ps1`
    * No Linux ou macOS: `source venv/bin/activate`

2.  **Instale as Dependências:**
    Com o ambiente virtual ativo:
    ```bash
    pip install Flask Flask-SQLAlchemy Flask-CORS
    ```

3.  **Crie o Banco de Dados e as Tabelas:**
    Você precisa criar o arquivo `site.db` e as tabelas definidas no seu modelo (`Item`). A forma recomendada com Flask CLI é:
    * Defina a variável de ambiente `FLASK_APP`:
        * Linux/macOS: `export FLASK_APP=app.py`
        * Windows (Cmd): `set FLASK_APP=app.py`
        * Windows (PowerShell): `$env:FLASK_APP="app.py"`
    * Execute o shell do Flask e crie as tabelas:
        ```bash
        flask shell
        ```
        Dentro do shell:
        ```python
        >>> from app import db
        >>> db.create_all()
        >>> exit()
        ```

4.  **Execute a Aplicação Flask:**
    Com o ambiente virtual ativo e `FLASK_APP` definido (se aplicável ao seu método), inicie o servidor de desenvolvimento:
    ```bash
    flask run
    ```

5.  **Verifique a Saída:**
    O terminal mostrará o endereço onde a API está rodando, geralmente `http://127.0.0.1:5000/`.

## 🧪 Como Testar a API

Com o servidor rodando, use ferramentas como **cURL**, **Postman**, **Insomnia** ou a extensão "REST Client" do VS Code para enviar requisições aos endpoints.

O endereço base para testes locais é `http://localhost:5000`.
## Code:
```bashfrom flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy # Importamos o SQLAlchemy

app = Flask(__name__)

# -- Configuração do banco de dados 
# Define a URI do banco de dados SQLite. O '//' duplo é por que o caminho é absoluto

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --Configuração do CORS ---
CORS(app)

# --- Definição do modelo de dados

class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=True)


    def __repr__(self):
        return f"Item('{self.name}', '{self.descricao}')"
    

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "descricao": self.descricao
        }
    

# --- Endpoint Básico (Página Inicial) ---
@app.route('/')
def index():
    return "Bem-vindo à API de Itens (com Banco de Dados!)"

# --- Endpoints da API ---
# -- Endpoint para listar todos os itens (GET) ---
@app.route('/itens', methods=['GET'])
def get_itens():
    # Consulta todos os objetos Item na tabela 'item'
    # O .all() executa a consulta e retorna uma lista de objetos Item
    todos_itens = Item.query.all()
    # Converte a lista de objetos Item para uma lista de dicionários usando o método to_dict()
    # list comprehension: [objeto.to_dict() for objeto in lista_de_objetos]
    return jsonify([item.to_dict() for item in todos_itens]), 200

# -- Endpoint para obter um item específico por ID (GET) ---
@app.route('/itens/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Consulta o item pelo ID. .get() é otimizado para buscar pela chave primária.
    # Se encontrado, retorna o objeto Item, caso contrário, retorna None
    item = Item.query.get(item_id)
    if item:
        # Se encontrado, retorna o dicionário do item
        return jsonify(item.to_dict()), 200
    # Se não encontrado, retorna o erro 404
    return jsonify({"error": "Item não encontrado"}), 404

# -- Endpoint para adicionar um novo item (POST) ---
@app.route('/itens', methods=['POST'])
def criar_item():
    # Pega os dados do corpo da requisição JSON
    novo_item_data = request.get_json()

    # Validação básica (ajustada para verificar "name" e "descricao" como no modelo)
    if not novo_item_data or 'name' not in novo_item_data or 'descricao' not in novo_item_data:
        return jsonify({"message": "Dados inválidos. Requer 'name' e 'descricao'."}), 400

    # Cria uma nova instância do modelo Item
    # Não precisamos definir o 'id', o banco de dados cuida do auto-incremento
    novo_item = Item(
        name=novo_item_data['name'],
        descricao=novo_item_data['descricao']
    )

    # Adiciona o novo item à sessão do banco de dados
    db.session.add(novo_item)
    # Salva as mudanças (o novo item) no banco de dados
    db.session.commit()

    # Retorna o item criado (agora ele terá o ID gerado pelo banco)
    return jsonify(novo_item.to_dict()), 201 # Status 201 (Created)

# -- Endpoint para atualizar um item existente (PUT) ---
@app.route('/itens/<int:item_id>', methods=['PUT'])
def atualizar_item(item_id):
    # Pega os dados do corpo da requisição JSON
    item_data = request.get_json()

    # Busca o item pelo ID
    item = Item.query.get(item_id)

    # Se o item não for encontrado, retorna 404
    if not item:
        return jsonify({"error": "Item não encontrado"}), 404

    # Atualiza os campos do item se os dados correspondentes existirem no JSON
    # Usamos .get() para evitar KeyError se a chave não estiver no JSON de entrada
    if item_data: # Verifica se item_data não é None ou vazio
        if 'name' in item_data:
            item.name = item_data['name']
        if 'descricao' in item_data:
            item.descricao = item_data['descricao']
        # Poderíamos usar .get() com valor padrão se preferir:
        # item.name = item_data.get('name', item.name)
        # item.descricao = item_data.get('descricao', item.descricao)


    # Salva as mudanças no banco de dados
    db.session.commit()

    # Retorna o item atualizado
    return jsonify(item.to_dict()), 200 # Status 200 (OK)

# -- Endpoint para deletar um item (DELETE) ---
@app.route('/itens/<int:item_id>', methods=['DELETE'])
def deletar_item(item_id):
    # Busca o item pelo ID
    item = Item.query.get(item_id)

    # Se o item não for encontrado, retorna 404
    if not item:
        return jsonify({"error": "Item não encontrado"}), 404

    # Deleta o item da sessão do banco de dados
    db.session.delete(item)
    # Salva as mudanças no banco de dados (executa a deleção)
    db.session.commit()

    # Retorna uma mensagem de sucesso
    return jsonify({"message": f"Item com ID {item_id} deletado com sucesso"}), 200 # Status 200 (OK)


# --- Execução do Servidor ---
if __name__ == '__main__':
    # Bloco para criar as tabelas (rode isso pelo menos uma vez)
    with app.app_context():
         db.create_all()
         # Opcional: Adicionar alguns dados iniciais se o banco estiver vazio
         # if not Item.query.first(): # Verifica se já tem algum item
         #    db.session.add(Item(name="Cadeira", descricao="Cadeira de escritório"))
         #    db.session.add(Item(name="Mesa", descricao="Mesa de escritório"))
         #    db.session.commit()


    # Roda o servidor Flask em modo debug
    app.run(debug=True)
```
**Exemplos de Requisições:**
### Cadastrando novo item:
- Methodo: POST
- Body:  

```bash
{
  "name": "Cadeira",
  "descricao": "Cadastrando"
}
```

![alt text](/src/assets/img/image.png)
=======
# Code:
```bash 
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Configuração do CORS - Permite requisições de qualquer origem
# É uma boa prática configurar o CORS logo após inicializar o app Flask
CORS(app)

# Nossa "base de dados" simples na memória
# Mantendo a consistência nas chaves: usando "name" e "descricao"
itens = [
    {"id": 1, "name": "Cadeira", "descricao": "Caidra de escritório"},
    {"id": 2, "name": "Mesa", "descricao": "Mesa de escritório"},
    {"id": 3, "name": "Monitor", "descricao": "Monitor de 24 polegadas"},
    {"id": 4, "name": "Teclado", "descricao": "Teclado mecânico"},
    {"id": 5, "name": "Mouse", "descricao": "Mouse sem fio"},
    {"id": 6, "name": "Impressora", "descricao": "Impressora a laser"},
    {"id": 7, "name": "Scanner", "descricao": "Scanner de mesa"},
    {"id": 8, "name": "Projetor", "descricao": "Projetor Full HD"},
    {"id": 9, "name": "Webcam", "descricao": "Webcam HD"},
    {"id": 10, "name": "Microfone", "descricao": "Microfone USB"}
]
# Variável global para o próximo ID
# Ajustado para snake_case (proximo_id) para seguir a convenção Python
proximo_id = 11

# --- Endpoints ---

# -- Endpoint para listar todos os itens (GET) ---
# URL: /itens
# Método: GET
# Corrigido: Adicionado a barra inicial '/' na rota
# Nome da função já estava correto nesta versão: get_itens
@app.route('/itens', methods=['GET'])
def get_itens():
    # Retornar a lista de itens em formato JSON com status 200 (OK)
    return jsonify(itens), 200

# -- Endpoint para obter um item específico por ID (GET) ---
# URL: /itens/<int:item_id>
# Método: GET
# Nome da função já estava ok: get_item
@app.route('/itens/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Procura o item na lista pelo ID
    for item in itens:
        if item['id'] == item_id:
            # Retorna o item encontrado em formato JSON com status 200 (OK)
            return jsonify(item), 200
    # Se o item não for encontrado, retorna um erro 404 (Not Found)
    # Mantendo a chave da mensagem de erro consistente ("error")
    return jsonify({"error": "Item não encontrado"}), 404

# -- Endpoint para adicionar um novo item (POST) ---
# URL: /itens
# Método: POST
# Corrigido: Nome da função ajustado para criar_item (snake_case)
@app.route('/itens', methods=['POST'])
def criar_item():
    # Corrigido: Referência correta à variável global com underscore (proximo_id)
    global proximo_id
    # Obtém os dados do item a partir do corpo da requisição (espera JSON)
    # request.get_json(force=True) pode ser útil se o content-type não for application/json
    novo_item_data = request.get_json()

    # Validação simples: verifica se as chaves "name" e "descricao" estão presentes
    # Ajustado para verificar "name" para consistência com a lista inicial
    if not novo_item_data or 'name' not in novo_item_data or 'descricao' not in novo_item_data:
         # Mantendo a chave da mensagem consistente ("message") para validação
         return jsonify({"message": "Dados inválidos. Requer 'name' e 'descricao'."}), 400 # Bad Request

    # Cria um novo item com o próximo ID
    # Usando "name" para consistência com a lista original
    novo_item = {
        # Corrigido: Usando a variável global com underscore (proximo_id)
        "id": proximo_id,
        "name": novo_item_data.get('name'), # Usando .get() é mais seguro caso a chave não venha
        "descricao": novo_item_data.get('descricao') # Usando .get()
    }
    # Adiciona o novo item à lista
    itens.append(novo_item)
    # Incrementa o próximo ID
    proximo_id += 1
    # Retorna o novo item criado em formato JSON com status 201 (Created)
    return jsonify(novo_item), 201

# -- Endpoint para atualizar um item existente (PUT) ---
# URL: /itens/<int:item_id>
# Método: PUT
# Nome da função já estava ok: atualizar_item
@app.route('/itens/<int:item_id>', methods=['PUT'])
def atualizar_item(item_id):
    # Obtém os dados do item a partir do corpo da requisição (espera JSON)
    item_data = request.get_json()

    # Procura o item na lista pelo ID
    for item in itens:
        if item['id'] == item_id:
            # Atualiza os dados do item se eles existirem no corpo da requisição
            # Usando item_data.get('chave', valor_padrao) é seguro
            # Ajustado para usar "name" para consistência com a lista original
            # Verifica se o dado existe no item_data antes de tentar usar .get()
            if item_data:
                item['name'] = item_data.get('name', item['name'])
                item['descricao'] = item_data.get('descricao', item['descricao'])
            # Retorna o item atualizado em formato JSON com status 200 (OK)
            return jsonify(item), 200

    # Se o item não for encontrado, retorna um erro 404 (Not Found)
    # Mantendo a chave da mensagem de erro consistente ("error")
    return jsonify({"error": "Item não encontrado"}), 404

# -- Endpoint para deletar um item (DELETE) ---
# URL: /itens/<int:item_id>
# Método: DELETE
# Nome da função já estava ok: deletar_item
@app.route('/itens/<int:item_id>', methods=['DELETE'])
def deletar_item(item_id):
    # Usando um loop para encontrar o item a ser removido
    # Iterar sobre uma cópia da lista é mais seguro se você for modificar (remover)
    # enquanto itera, mas o seu código original funcionava aqui porque ele
    # retorna logo após encontrar e remover.
    # Vamos usar uma abordagem comum e segura com list comprehension para estudo.
    global itens # Precisamos dizer que vamos reatribuir a variável global itens
    initial_item_count = len(itens) # Guarda o tamanho inicial

    # Cria uma nova lista 'itens' contendo apenas os itens cujo ID não corresponde ao item_id
    itens = [item for item in itens if item['id'] != item_id]

    # Verifica se algum item foi removido comparando o tamanho da lista
    if len(itens) < initial_item_count:
        # Retorna uma mensagem de sucesso consistente ("message") com status 200 (OK)
        return jsonify({"message": f"Item com ID {item_id} deletado com sucesso"}), 200
    else:
        # Se o tamanho não mudou, o item não foi encontrado. Retorna erro 404.
        # Mantendo a chave da mensagem de erro consistente ("error")
        return jsonify({"error": f"Item com ID {item_id} não encontrado"}), 404


# -- Endpoint Básico (Página Inicial) ---
@app.route('/')
def index():
    return "Bem-vindo à API de Itens!"

# -- Execução do Servidor ---
# Roda o servidor Flask quando o script é executado diretamente
if __name__ == '__main__':
    # debug=True reinicia o servidor automaticamente ao salvar e mostra erros detalhados
    app.run(debug=True)

# Comentários adicionais sobre como testar a API
# O servidor Flask será executado em http://localhost:5000
# Você pode testar os endpoints usando ferramentas como Postman, Insomnia ou cURL.
#
# Exemplos de requisições:
# - GET http://localhost:5000/itens
# - POST http://localhost:5000/itens (Corpo JSON: {"name": "Novo Item", "descricao": "Descrição do novo item"})
# - GET http://localhost:5000/itens/1
# - PUT http://localhost:5000/itens/1 (Corpo JSON: {"descricao": "Nova descrição"})
# - DELETE http://localhost:5000/itens/1
```
>>>>>>> 6067594a5cf7a90cc90932c8e71931189211005e
