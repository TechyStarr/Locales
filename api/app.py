from flask import Flask, render_template
from auth.web_views import auth
from .search.web_views import views

app = Flask(__name__)





app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')


if __name__ == '__main__':
    app.run()
