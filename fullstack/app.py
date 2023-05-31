from flask import Flask, render_template
from backend.views import views
# from backend.users import user

app = Flask(__name__)

# Register the API blueprint
# app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(views, url_prefix='/views')



if __name__ == '__main__':
    app.run()
