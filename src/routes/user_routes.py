from flask import Blueprint
from src.controllers.user_controller import get_list, add_user_form, inser_user

user_routes = Blueprint("user_routes", __name__)
user_routes.route("/user/list/", methods=["GET"])(get_list)
user_routes.route("/user/addForm/")(add_user_form)
user_routes.route("/user/add/", methods=["POST"])(inser_user)

# user_routes.route('/user/update/<int:user_id>', methods=['PUT'])(update_user)
