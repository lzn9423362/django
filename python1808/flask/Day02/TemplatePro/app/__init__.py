from flask import Flask

from app.views import blue


def init_app():
    app = Flask(__name__)
    app.register_blueprint(blue)
    return app