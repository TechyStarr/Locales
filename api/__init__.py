from flask import Flask
from flask_restx import Api
from .auth.views import auth_namespace
from .search.views import search_namespace
from .config.config import config_dict
from .utils.utils import db
from .models.users import User
from .models.data import Region, State, Lga, Area
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager




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
    api.add_namespace(search_namespace, path='/search')



    @app.shell_context_processor 
    def make_shell_context():
        return {
            'db': db,
            'User': User,
            'Region': Region,
            'State': State,
            'Lga': Lga,
            'Area': Area
        }




    return app
