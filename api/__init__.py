from flask import Flask
from flask_restx import Api
# from .config.config import config_dict
from .utils import db



def create_app():
    app = Flask(__name__)

    # app.config.from_object(config)

    db.init_app(app)





    return app