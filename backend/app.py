# app.py
from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from models import db, Customer, Product, Order, OrderDetail, Payment, Address, Admin

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)  # Habilitar CORS para todas as rotas
db.init_app(app)

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{
        'customerid': customer.customerid,
        'firstname': customer.firstname,
        'lastname': customer.lastname,
        'email': customer.email,
        'registeredat': customer.registeredat,
        'profileupdatedat': customer.profileupdatedat
    } for customer in customers])

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
        'updatedat': product.updatedat
    } for product in products])

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{
        'orderid': order.orderid,
        'customerid': order.customerid,
        'orderdate': order.orderdate,
        'status': order.status,
        'totalamount': float(order.totalamount)
    } for order in orders])

@app.route('/orderdetails', methods=['GET'])
def get_orderdetails():
    orderdetails = OrderDetail.query.all()
    return jsonify([{
        'orderdetailid': orderdetail.orderdetailid,
        'orderid': orderdetail.orderid,
        'productid': orderdetail.productid,
        'quantity': orderdetail.quantity,
        'price': float(orderdetail.price)
    } for orderdetail in orderdetails])

@app.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([{
        'paymentid': payment.paymentid,
        'orderid': payment.orderid,
        'paymentdate': payment.paymentdate,
        'amount': float(payment.amount),
        'paymentmethod': payment.paymentmethod,
        'status': payment.status
    } for payment in payments])

@app.route('/addresses', methods=['GET'])
def get_addresses():
    addresses = Address.query.all()
    return jsonify([{
        'addressid': address.addressid,
        'customerid': address.customerid,
        'addressline1': address.addressline1,
        'addressline2': address.addressline2,
        'city': address.city,
        'state': address.state,
        'zipcode': address.zipcode,
        'country': address.country
    } for address in addresses])

@app.route('/admins', methods=['GET'])
def get_admins():
    admins = Admin.query.all()
    return jsonify([{
        'adminid': admin.adminid,
        'username': admin.username,
        'createdat': admin.createdat
    } for admin in admins])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)
