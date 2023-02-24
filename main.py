from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from src.models.shared import db
from src.routes.users_routes import users_routes

# import importlib
# importlib.reload(module)
# sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
# db = SQLAlchemy(app)
CORS(app)

app.register_blueprint(users_routes)



@app.before_first_request
def initialize_database():
    db.create_all()


@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()


@app.route('/tesst/', methods=['GET'])
def index():
    return "Test API"


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
