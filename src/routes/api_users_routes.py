from flask import Blueprint
from src.controllers.api_user_controller import get_list, get_user, insert_user, update_user, insert_user_native_query, get_list_native_query, update_user_native_query

users_routes = Blueprint("users_routes", __name__)
users_routes.route("/api/user_list/", methods=["GET"])(get_list)
users_routes.route("/api/user/<int:user_id>", methods=['GET'])(get_user)
users_routes.route("/api/user_add/", methods=['POST'])(insert_user)
users_routes.route("/api/user_update/<int:user_id>",
                   methods=['POST'])(update_user)

# API call fnc using nativeQuery
users_routes.route("/api/user_list_1/", methods=["GET"])(get_list_native_query)
users_routes.route(
    "/api/user_add_1/", methods=['POST'])(insert_user_native_query)
users_routes.route("/api/user_update_1/<int:user_id>",
                   methods=['POST'])(update_user_native_query)
