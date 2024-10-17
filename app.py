from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin #lib flask para login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)
CORS(app)

#Modelagem 

#User (id, username, password)
#Usando o UserMixin como herança que já possui várias funções definidas
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=True)

#Produto(id, name, price, description)
class Product(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

@app.route('/api/products/add', methods=['POST'])
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description",""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message":"Product added successfully"}), 200
    return jsonify({"message":"Invalid product data"}), 400

@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    #Recuperar o produto da base de dados
    #Verificar se o produto existe
    #Se existe, apagar na base de dados
    #Se não existe, retornar 404 not found
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message":"Product deleted successfully"}), 200
    return jsonify({"message":"Product not found!"}), 404

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id":product.id,
            "name":product.name,
            "price":product.price,
            "description":product.description
        }), 200
    return jsonify({"message":"Product not found!"}), 404

@app.route('/api/products/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message":"Product not found!"}), 404
    data = request.json
    if 'name' in data:
        product.name = data['name']
    if 'price' in data:
        product.price = data['price']
    if 'description' in data:
        product.description = data['description']

    db.session.commit()

    return jsonify({"message":"Product update successfully"}), 200

@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [] # criar uma lista
    for product in products: 
        product_data = {
            "id":product.id,
            "name":product.name,
            "price":product.price,
            "description":product.description
        }
        product_list.append(product_data)
    return jsonify(product_list), 200

    # começa por arqui
    # products = Product.query.all()
    # print(products)
    # for product in products:
    # mostra a lista que vem do banco
    # 1
    #   print(product)
    # 2 o return e mostra no postman somente o 1º pq temos o return e daí ele sai
    #     return jsonify({
    #         "id":product.id,
    #         "name":product.name,
    #         "price":product.price,
    #         "description":product.description
    #     }), 200
    # return jsonify({"message":"Test"}), 200


# Definir uma rota raiz inicial e a função que será executada quando for requisitada
@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Isso cria as tabelas no banco de dados
    app.run(debug=True)