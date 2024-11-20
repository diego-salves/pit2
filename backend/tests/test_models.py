import pytest
from app import app, db
from models import Customer, Product, Order, OrderDetail, Payment, Address, Admin

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Usando SQLite para testes
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Adicionando dados de exemplo
            customer = Customer(firstname='John', lastname='Doe', email='john.doe@example.com', passwordhash='hashed_password')
            db.session.add(customer)
            db.session.commit()
            
            product = Product(name='Cupcake de Chocolate', description='Delicioso cupcake de chocolate', price=2.99, stock=50)
            db.session.add(product)
            db.session.commit()
            
            order = Order(customerid=customer.customerid, status='Pending', totalamount=29.99)
            db.session.add(order)
            db.session.commit()
            
            order_detail = OrderDetail(orderid=order.orderid, productid=product.productid, quantity=3, price=2.99)
            db.session.add(order_detail)
            db.session.commit()
            
            payment = Payment(orderid=order.orderid, amount=29.99, paymentmethod='Credit Card', status='Completed')
            db.session.add(payment)
            db.session.commit()
            
            address = Address(customerid=customer.customerid, addressline1='123 Main St', city='Anytown', state='CA', zipcode='12345', country='USA')
            db.session.add(address)
            db.session.commit()
            
            admin = Admin(username='admin', passwordhash='admin_hashed_password')
            db.session.add(admin)
            db.session.commit()
            
            yield client
            db.drop_all()

def test_create_customer(client):
    with app.app_context():
        customer = Customer(firstname='Jane', lastname='Doe', email='jane.doe@example.com', passwordhash='hashed_password')
        db.session.add(customer)
        db.session.commit()
        assert customer in db.session

def test_get_customers(client):
    with app.app_context():
        customer = Customer.query.filter_by(email='jane.doe@example.com').first()
        assert customer is not None
        assert customer.firstname == 'Jane'
        assert customer.lastname == 'Doe'
        assert customer.email == 'jane.doe@example.com'

def test_create_product(client):
    with app.app_context():
        product = Product(name='Cupcake de Chocolate', description='Delicioso cupcake de chocolate', price=2.99, stock=50)
        db.session.add(product)
        db.session.commit()
        assert product in db.session

def test_get_products(client):
    with app.app_context():
        products = Product.query.all()
        assert len(products) > 0

def test_create_order(client):
    with app.app_context():
        customer = Customer.query.filter_by(email='jane.doe@example.com').first()
        order = Order(customerid=customer.customerid, status='Pending', totalamount=29.99)
        db.session.add(order)
        db.session.commit()
        assert order in db.session

def test_get_orders(client):
    with app.app_context():
        orders = Order.query.all()
        assert len(orders) > 0

def test_create_order_detail(client):
    with app.app_context():
        customer = Customer.query.filter_by(email='jane.doe@example.com').first()
        product = Product.query.filter_by(name='Cupcake de Chocolate').first()
        order = Order.query.filter_by(customerid=customer.customerid).first()
        order_detail = OrderDetail(orderid=order.orderid, productid=product.productid, quantity=3, price=2.99)
        db.session.add(order_detail)
        db.session.commit()
        assert order_detail in db.session

def test_get_orderdetails(client):
    with app.app_context():
        orderdetails = OrderDetail.query.all()
        assert len(orderdetails) > 0

def test_create_payment(client):
    with app.app_context():
        order = Order.query.first()
        payment = Payment(orderid=order.orderid, amount=29.99, paymentmethod='Credit Card', status='Completed')
        db.session.add(payment)
        db.session.commit()
        assert payment in db.session

def test_get_payments(client):
    with app.app_context():
        payments = Payment.query.all()
        assert len(payments) > 0

def test_create_address(client):
    with app.app_context():
        customer = Customer.query.filter_by(email='jane.doe@example.com').first()
        address = Address(customerid=customer.customerid, addressline1='123 Main St', city='Anytown', state='CA', zipcode='12345', country='USA')
        db.session.add(address)
        db.session.commit()
        assert address in db.session

def test_get_addresses(client):
    with app.app_context():
        addresses = Address.query.all()
        assert len(addresses) > 0

def test_create_admin(client):
    with app.app_context():
        admin = Admin(username='admin', passwordhash='admin_hashed_password')
        db.session.add(admin)
        db.session.commit()
        assert admin in db.session

def test_get_admins(client):
    with app.app_context():
        admins = Admin.query.all()
        assert len(admins) > 0
