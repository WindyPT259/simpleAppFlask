from src.models.users import User
from src.models.shared import db
from flask import json, jsonify, request


def home():
    return "hello Thẽo thẽo"


def get_list():
    users = User.query.all()

    users_list = []
    for user in users:
        user_json = {
            'id': user.id,
            'username': user.username,
            'full_name': user.full_name,
            'email': user.email,
            'phone_number': user.phone_number,
            'report_access': user.report_access,
            'view_costs': user.view_costs,
            'last_login_date': user.last_login_date,
            'enabled': user.enabled,
            'is_corporated': user.is_corporated,
            'created_on': user.created_on,
            'modified_on': user.modified_on,
        }
        users_list.append(user_json)
    return jsonify(users_list)


def inser_user():
    username = request.json['username']
    full_name = request.json['full_name']
    email = request.json['email']
    phone_number = request.json['phone_number']
    report_access = request.json['report_access']
    view_costs = request.json['view_costs']
    last_login_date = request.json['last_login_date']
    enabled = request.json['enabled']
    is_corporated = request.json['is_corporated']
    created_on = request.json['created_on']
    modified_on = request.json['modified_on']

    user = User(
        username,
        full_name,
        email,
        phone_number,
        report_access,
        view_costs,
        last_login_date,
        enabled,
        is_corporated,
        created_on,
        modified_on)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'})


def uppdate_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    user.username = data['username']
    user.full_name = data['full_name']
    user.email = data['email']
    user.phone_number = data['phone_number']
    user.report_access = data['report_access']
    user.view_costs = data['view_costs']
    user.last_login_date = data['last_login_date']
    user.enabled = data['enabled']
    user.is_corporated = data['is_corporated']
    user.created_on = data['created_on']
    user.modified_on = data['modified_on']

    db.session.commit()

    return jsonify({'message': 'User updated successfully'})
