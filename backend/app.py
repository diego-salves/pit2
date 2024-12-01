from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config
from models import db, Customer, Product, Order, OrderDetail, Payment, Address, Admin
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)  # Habilitar CORS para todas as rotas
db.init_app(app)

@app.route('/admins/login', methods=['POST'])
def login_admin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    admin = Admin.query.filter_by(username=username).first()
    if admin and check_password_hash(admin.passwordhash, password):
        return jsonify({
            'adminid': admin.adminid,
            'username': admin.username
        })
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        'productid': product.productid,
        'name': product.name,
        'description': product.description,
        'price': float(product.price),
        'stock': product.stock,
        'createdat': product.createdat,
        'updatedat': product.updatedat,
        'adminid': product.adminid
    } for product in products])

@app.route('/products/<int:productid>', methods=['GET'])
def get_product(productid):
    product = Product.query.get_or_404(productid)
    return jsonify({
        'productid': product.productid,
        'name': product.name,
        'description': product.description,
        'price': float(product.price),
        'stock': product.stock,
        'createdat': product.createdat,
        'updatedat': product.updatedat,
        'adminid': product.adminid
    })

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        stock=data['stock'],
        adminid=data['adminid'],  # Associa o produto ao administrador
        createdat=db.func.current_timestamp(),
        updatedat=db.func.current_timestamp()
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({
        'productid': new_product.productid,
        'name': new_product.name,
        'description': new_product.description,
        'price': float(new_product.price),
        'stock': new_product.stock,
        'createdat': new_product.createdat,
        'updatedat': new_product.updatedat,
        'adminid': new_product.adminid
    }), 201

@app.route('/products/<int:productid>', methods=['PUT'])
def update_product(productid):
    product = Product.query.get_or_404(productid)
    data = request.get_json()
    product.name = data['name']
    product.description = data['description']
    product.price = data['price']
    product.stock = data['stock']
    product.adminid = data['adminid']  # Associa o produto ao administrador
    product.updatedat = db.func.current_timestamp()
    db.session.commit()
    return jsonify({
        'productid': product.productid,
        'name': product.name,
        'description': product.description,
        'price': float(product.price),
        'stock': product.stock,
        'createdat': product.createdat,
        'updatedat': product.updatedat,
        'adminid': product.adminid
    })

@app.route('/products/<int:productid>', methods=['DELETE'])
def delete_product(productid):
    product = Product.query.get_or_404(productid)
    db.session.delete(product)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)