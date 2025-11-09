from flask import Flask
from app.db import db
from app.utils.loader import load_routes_from_yaml
from flask_migrate import Migrate


migrate = Migrate()
def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Initialize database
    db.init_app(app)
    migrate.init_app(app, db)

    # Load routes dynamically from routes.yaml
    load_routes_from_yaml(app, "app/routes.yaml")

    with app.app_context():
        db.create_all()  # Create tables on first run

    return app
