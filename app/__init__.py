import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app import characters

    app.register_blueprint(characters.bp)

    return app