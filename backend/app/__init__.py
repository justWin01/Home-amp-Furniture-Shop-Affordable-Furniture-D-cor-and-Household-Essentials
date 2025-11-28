from flask import Flask, jsonify
from extensions import db, jwt, cors
from config import Config

from app.routes import register_routes


def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    # Root route
    @app.route("/")
    def home():
        return "<h2>Backend is running!</h2><p>Go to <a href='/api'>/api</a> for API endpoints</p>"

    # API documentation route
    @app.get("/api")
    def api_info():  
        return jsonify({
            "endpoints": {
                "users": "Full CRUD at /api/auth",
                "categories": "Full CRUD at /api/categories",
                "products": "Full CRUD at /api/products",
                "orders": "Full CRUD at /api/orders",
                "order_details": "Full CRUD at /api/order-details"
            }
        })

    # Register all blueprints
    register_routes(app)

    # Create all tables
    with app.app_context():
        db.create_all()

    return app
