from extensions import db

class Orders(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    order_date = db.Column(db.DateTime, server_default=db.func.now())
    total_amount = db.Column(db.Numeric(10,2), default=0.00)
    status = db.Column(db.Enum('Pending','Shipped','Completed','Cancelled'), default='Pending')

    customer = db.relationship('User', backref='orders')

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'customer_id': self.customer_id,
            'order_date': self.order_date.isoformat(),
            'total_amount': float(self.total_amount),
            'status': self.status
        }
