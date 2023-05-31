from flask import Flask, render_template
from views.views import views
from views.auth import auth

app = Flask(__name__)





app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')


if __name__ == '__main__':
    app.run()
