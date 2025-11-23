def register_routes(app):
    from app.controllers.user_controller import user_bp
    from app.controllers.category_controller import category_bp
    from app.controllers.product_controller import product_bp
    from app.controllers.orders_controller import orders_bp
    from app.controllers.order_details_controller import order_details_bp

    app.register_blueprint(user_bp, url_prefix="/api")
    app.register_blueprint(category_bp, url_prefix="/api")
    app.register_blueprint(product_bp, url_prefix="/api")
    app.register_blueprint(orders_bp, url_prefix="/api")
    app.register_blueprint(order_details_bp, url_prefix="/api")
