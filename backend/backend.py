from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/home_furniture_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ------------------------
# Models
# ------------------------
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    contact_number = db.Column(db.String(20))
    address = db.Column(db.Text)
    role = db.Column(db.Enum('Admin', 'Customer'), default='Customer')

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100))
    description = db.Column(db.Text)

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(150))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    stock_quantity = db.Column(db.Integer)
    image = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))

class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Float)
    status = db.Column(db.Enum('Pending', 'Shipped', 'Completed', 'Cancelled'), default='Pending')

class OrderDetails(db.Model):
    order_detail_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    quantity = db.Column(db.Integer)
    subtotal = db.Column(db.Float)

# ------------------------
# Routes
# ------------------------

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            "id": p.product_id,
            "name": p.product_name,
            "price": p.price,
            "stock": p.stock_quantity
        } for p in products
    ])

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Orders(
        customer_id=data['customer_id'],
        total_amount=data['total_amount'],
        status='Pending'
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order created successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
