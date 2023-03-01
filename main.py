from flask import Flask, render_template
from flask_cors import CORS
from src.models.shared import db
from src.routes.api_users_routes import users_routes
from src.routes.user_routes import user_routes as base_routes

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
# db = SQLAlchemy(app)
CORS(app)

app.register_blueprint(users_routes)
app.register_blueprint(base_routes)


@app.before_first_request
def initialize_database():
    db.create_all()


@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()


# with app.app_context():
#     db.create_all()

# errors
@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
