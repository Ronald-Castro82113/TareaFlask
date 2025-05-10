from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuración de la app
    app.config.from_object(Config)

    # Inicialización de las extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    from app import models
    from app.routes.libros import libros_bp
    from app.routes.home import home_bp

    # Registrar Blueprints
    app.register_blueprint(libros_bp)
    app.register_blueprint(home_bp)

    return app