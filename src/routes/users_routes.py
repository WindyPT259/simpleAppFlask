from flask import Blueprint
from src.controllers.user_controller import get_list, home, inser_user, uppdate_user

users_routes = Blueprint("users_routes", __name__)
users_routes.route("/", methods=["GET"])(get_list)
users_routes.route("/user/add/", methods=['POST'])(inser_user)
users_routes.route('/user/update/<int:user_id>', methods=['PUT'])(uppdate_user)
