from flask import Blueprint
from src.controllers.api_user_controller import get_list, inser_user, update_user

users_routes = Blueprint("users_routes", __name__)
users_routes.route("/api/user_list/", methods=["GET"])(get_list)
users_routes.route("/api/user_add/", methods=['POST'])(inser_user)
users_routes.route('/api/user_update/<int:user_id>',
                   methods=['PUT'])(update_user)
