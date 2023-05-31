from flask import Flask, render_template
from backend.views import auth

app = Flask(__name__)

# Register the API blueprint
app.register_blueprint(auth, url_prefix='/api')

# Define your website routes
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
