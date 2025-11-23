from flask import Blueprint
from .controllers.user_controller import user_bp
from .controllers.category_controller import category_bp
from .controllers.product_controller import product_bp
from .controllers.orders_controller import orders_bp
from .controllers.order_details_controller import order_details_bp

def register_routes(app):
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(category_bp, url_prefix='/api/categories')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(orders_bp, url_prefix='/api/orders')
    app.register_blueprint(order_details_bp, url_prefix='/api/order-details')
