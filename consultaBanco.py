from flask import Flask, jsonify, request
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