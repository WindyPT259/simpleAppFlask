from flask import Blueprint
from src.controllers.user_controller import get_list, add_user_form, insert_user, update_user, update_user_form

user_routes = Blueprint("user_routes", __name__)
user_routes.route("/", methods=["GET"])(get_list)
user_routes.route("/user/add/", methods=["POST"])(insert_user)
user_routes.route('/user/update/<int:user_id>', methods=['POST'])(update_user)
user_routes.route("/user/addForm/")(add_user_form)
user_routes.route("/user/updateForm/<int:user_id>",
                  methods=['GET'])(update_user_form)
