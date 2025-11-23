from flask import Flask
from config import Config
from extensions import db, bcrypt, jwt
from flask_cors import CORS
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Correct CORS usage
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Root route
    @app.route('/')
    def home():
        return "Flask backend is running!"

    # Register blueprints
    register_routes(app)

    return app
