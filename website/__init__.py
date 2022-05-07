from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "26c3189005da783b206cf1d37747d8f3f593536d"

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
