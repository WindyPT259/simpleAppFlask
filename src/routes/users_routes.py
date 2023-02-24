from flask import Blueprint
from src.controllers.user_controller import get_list, home

users_routes = Blueprint ("users_routes", __name__)
users_routes.route("/")(home)
users_routes.route("/user/list/", methods = ["POST"])(get_list)