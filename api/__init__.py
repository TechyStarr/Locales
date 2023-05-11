from flask import Flask
from flask_restx import Api
from .config.config import config_dict
# from .utils import db
from .auth.views import auth_namespace

from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import NotFound, MethodNotAllowed



def create_app(config=config_dict['dev']):
    app = Flask(__name__)

    app.config.from_object(config)

    # db.init_app(app)


    api = Api(app,
        title="Locale API", 
        description="Find whatever you're looking for using Locale API",
        # authorization = authorizations,
        # security = "Bearer Auth"
    )

    api.add_namespace(auth_namespace, path='/auth')



    @app.shell_context_processor 
    def make_shell_context():
        return {
        }


    return app
