from flask import Flask, render_template
from website.views.views import views
from website.views.auth import auth
# from models.users import db
from flask_sqlalchemy import SQLAlchemy
import os


# app = Flask(__name__)




base_dir = os.path.dirname(os.path.realpath(__file__))


# def create_app():
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + \
    os.path.join(base_dir,'db.sqlite3')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = 'iLhqyLO3HtSpsE8cuQaj'
db = SQLAlchemy(app)
db.init_app(app)






app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')


if __name__ == '__main__':
    # app = create_app()
    app.run()
