from flask import Flask
from .backend.users import auth
# from .backend.views import views

app = Flask(__name__)

# Register the API blueprint
app.register_blueprint(auth)

# Register the website blueprint
# app.register_blueprint(views)

if __name__ == '__main__':
    app.run()
