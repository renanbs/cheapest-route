from flask import Flask

from api.rest import routes


def create_app() -> Flask:
    app_flask = Flask(__name__)
    app_flask.register_blueprint(routes.bp)

    return app_flask
