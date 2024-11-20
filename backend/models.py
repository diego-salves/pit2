from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'
    customerid = db.Column(db.Integer, primary_key=True)  # Usando minúsculas
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    passwordhash = db.Column(db.String(255))
    registeredat = db.Column(db.DateTime)
    profileupdatedat = db.Column(db.DateTime)

class Product(db.Model):
    __tablename__ = 'products'
    productid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2))
    stock = db.Column(db.Integer)
    createdat = db.Column(db.DateTime)
    updatedat = db.Column(db.DateTime)

class Order(db.Model):
    __tablename__ = 'orders'
    orderid = db.Column(db.Integer, primary_key=True)
    customerid = db.Column(db.Integer, db.ForeignKey('customers.customerid'), nullable=False)
    orderdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(50))
    totalamount = db.Column(db.Numeric(10, 2))

    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))

class OrderDetail(db.Model):
    __tablename__ = 'orderdetails'
    orderdetailid = db.Column(db.Integer, primary_key=True)
    orderid = db.Column(db.Integer, db.ForeignKey('orders.orderid'), nullable=False)
    productid = db.Column(db.Integer, db.ForeignKey('products.productid'), nullable=False)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Numeric(10, 2))

    order = db.relationship('Order', backref=db.backref('orderdetails', lazy=True))
    product = db.relationship('Product', backref=db.backref('orderdetails', lazy=True))

class Payment(db.Model):
    __tablename__ = 'payments'
    paymentid = db.Column(db.Integer, primary_key=True)
    orderid = db.Column(db.Integer, db.ForeignKey('orders.orderid'), nullable=False)
    paymentdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    amount = db.Column(db.Numeric(10, 2))
    paymentmethod = db.Column(db.String(50))
    status = db.Column(db.String(50))

    order = db.relationship('Order', backref=db.backref('payments', lazy=True))

class Address(db.Model):
    __tablename__ = 'addresses'
    addressid = db.Column(db.Integer, primary_key=True)
    customerid = db.Column(db.Integer, db.ForeignKey('customers.customerid'), nullable=False)
    addressline1 = db.Column(db.String(255))
    addressline2 = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    zipcode = db.Column(db.String(20))
    country = db.Column(db.String(100))

    customer = db.relationship('Customer', backref=db.backref('addresses', lazy=True))

class Admin(db.Model):
    __tablename__ = 'admins'
    adminid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    passwordhash = db.Column(db.String(255))
    createdat = db.Column(db.DateTime, default=db.func.current_timestamp())
