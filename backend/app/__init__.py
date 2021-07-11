from flask import Flask


def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 注册 blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app