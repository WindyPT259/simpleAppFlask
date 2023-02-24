from flask import Flask, render_template
from flask_cors import CORS

from src.routes.users_routes import users_routes
from src.models import *

app = Flask (__name__)
app.config.from_pyfile('config.py')
CORS (app)

app.register_blueprint(users_routes)


#errors
@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html')

if __name__ == '__main__':
    app.run() 