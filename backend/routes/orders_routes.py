from flask import Blueprint, request, jsonify
from models import db, Orders

orders_bp = Blueprint('orders_bp', __name__)

# GET all orders
@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Orders.query.all()
    return jsonify([{
        'order_id': o.order_id,
        'customer_id': o.customer_id,
        'order_date': o.order_date.isoformat(),
        'total_amount': o.total_amount,
        'status': o.status
    } for o in orders])

# POST new order
@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    order = Orders(
        customer_id=data['customer_id'],
        total_amount=data['total_amount'],
        status=data.get('status', 'Pending')
    )
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Order created', 'order_id': order.order_id})
