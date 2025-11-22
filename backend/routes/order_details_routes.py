from flask import Blueprint, request, jsonify
from models import db, OrderDetails

order_details_bp = Blueprint('order_details_bp', __name__)

# GET all order details
@order_details_bp.route('/order-details', methods=['GET'])
def get_order_details():
    details = OrderDetails.query.all()
    return jsonify([{
        'order_detail_id': d.order_detail_id,
        'order_id': d.order_id,
        'product_id': d.product_id,
        'quantity': d.quantity,
        'subtotal': d.subtotal
    } for d in details])

# POST new order detail
@order_details_bp.route('/order-details', methods=['POST'])
def create_order_detail():
    data = request.get_json()
    detail = OrderDetails(
        order_id=data['order_id'],
        product_id=data['product_id'],
        quantity=data['quantity'],
        subtotal=data['subtotal']
    )
    db.session.add(detail)
    db.session.commit()
    return jsonify({'message': 'OrderDetail created', 'order_detail_id': detail.order_detail_id})
