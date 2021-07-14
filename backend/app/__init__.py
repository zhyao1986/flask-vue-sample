from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Flask-SQLAlchemy plugin
db = SQLAlchemy()
# Flask-Migrate plugin
migrate = Migrate()


def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False

    # enable CORS
    CORS(app)
    # Init Flask-SQLAlchemy
    db.init_app(app)
    # Init Flask-Migrate
    migrate.init_app(app, db)

    # 注册 blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


from app import models
