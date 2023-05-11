from flask import Flask
from flask_restx import Api
from .auth.views import auth_namespace
from .config.config import config_dict
from .utils.utils import db

from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import NotFound, MethodNotAllowed



def create_app(config=config_dict['dev']):
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)

    jwt = JWTManager(app)

    migrate = Migrate(app, db)

    # authorizations = {
    #     "Bearer Auth": {
    #     "type": "apikey",
    #     "in": "header",
    #     "name": "Authorization", 
    #     "description": "Add a JWT token to the header with ** Bearer &lt;JWT&gt; ** token to authorize user "
    #     }
    # }

    api = Api(app,
        title="Locale API", 
        description="Find whatever you're looking for using Locale",
        # authorization = authorizations,
        # security = "Bearer Auth"
    )

    api.add_namespace(auth_namespace, path='/auth')



    return app
