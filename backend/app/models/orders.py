from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from extensions import db

db = SQLAlchemy()

class Orders(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum('Pending', 'Shipped', 'Completed', 'Cancelled'), default='Pending', nullable=False)

    order_details = db.relationship('OrderDetails', backref='order', lazy=True)
