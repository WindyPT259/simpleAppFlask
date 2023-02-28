from src.models.users import User
from src.models.shared import db
from flask import jsonify, request
from sqlalchemy import text


# GET LIST USER
def get_list():
    try:
        query = text(
            "SELECT column_name FROM information_schema.columns WHERE table_name = 'user' AND table_schema = 'sampleapp'")
        columns = db.session.execute(query)
        column_names = [column[0] for column in columns]
        users = User.query.all()
        users_data = []
        for user in users:
            user_data = {}
            for column_name in column_names:
                user_data[column_name] = getattr(user, column_name)
            users_data.append(user_data)

        results = {
            "status_code": 200,
            "success": True,
            "data": {"userList": users_data, "headerList": column_names}
        }
    except Exception as e:
        results = {
            "status_code": 500,
            "success": False,
            "message": str(e)
        }
    return jsonify(results)


# GET USER
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    if user:
        return jsonify({
            'success': True,
            'status_code': 200,
            'data': {
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
        })
    else:
        return jsonify({
            'success': False,
            "status_code": 500,
            'message': 'User not found'
        })


# INSERT USER
def insert_user():
    try:
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

        user = User(username, full_name, email, phone_number, report_access, view_costs,
                    last_login_date, enabled, is_corporated, created_on, modified_on)
        db.session.add(user)
        db.session.commit()
        results = {
            "status_code": 200,
            "success": True,
        }
    except Exception as e:
        results = {
            "status_code": 500,
            "success": False,
            "message": str(e)
        }
    return jsonify(results)


# UPDATE USER
def update_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        if user:
            data = request.get_json()  # data to json

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

            results = {
                "status_code": 200,
                "success": True,
                'message': 'User updated successfully'
            }
    except Exception as e:
        results = {
            "status_code": 500,
            "success": False,
            "message": str(e)
        }
    return jsonify(results)

### ------API get data using nativeQuery------------------------------------------------------########


# GET LIST USER
def get_list_native_query():
    try:
        query = text(
            "SELECT column_name FROM information_schema.columns WHERE table_name = 'user' AND table_schema = 'sampleapp'")
        columns = db.session.execute(query)
        column_names = [column[0] for column in columns]

        query = text(
            "SELECT * FROM user")
        users = db.session.execute(query)
        users_data = []
        for user in users:
            user_data = {}
            for column_name in column_names:
                user_data[column_name] = getattr(user, column_name)
            users_data.append(user_data)

        results = {
            "status_code": 200,
            "success": True,
            "data": {"userList": users_data, "headerList": column_names}
        }
    except Exception as e:
        results = {
            "status_code": 500,
            "success": False,
            "message": str(e)
        }
    return jsonify(results)


# INSERT USER
def insert_user_native_query():
    try:
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

        query = text(
            "INSERT INTO user (username, full_name, email, phone_number, report_access, view_costs, last_login_date, enabled, is_corporated, created_on, modified_on) VALUES (:username, :full_name, :email, :phone_number, :report_access, :view_costs, :last_login_date, :enabled, :is_corporated, :created_on, :modified_on)")
        db.session.execute(query, {
            'username': username,
            'full_name': full_name,
            'email': email,
            'phone_number': phone_number,
            'report_access': report_access,
            'view_costs': view_costs,
            'last_login_date': last_login_date,
            'enabled': enabled,
            'is_corporated': is_corporated,
            'created_on': created_on,
            'modified_on': modified_on
        })
        db.session.commit()
        results = {
            "status_code": 200,
            "success": True,
        }
    except Exception as e:
        results = {
            "status_code": 500,
            "success": False,
            "message": str(e)
        }
    return jsonify(results)


# UPDATE USER
def update_user_native_query(user_id):
    try:
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

        query = text(
            "UPDATE user SET username=:username, full_name=:full_name, email=:email, phone_number=:phone_number, "
            "report_access=:report_access, view_costs=:view_costs, last_login_date=:last_login_date, enabled=:enabled, "
            "is_corporated=:is_corporated, created_on =:created_on , modified_on=:modified_on WHERE id=:user_id")
        db.session.execute(query, {'username': username, 'full_name': full_name, 'email': email,
                                   'phone_number': phone_number, 'report_access': report_access,
                                   'view_costs': view_costs, 'last_login_date': last_login_date,
                                   'enabled': enabled, 'is_corporated': is_corporated, 'created_on': created_on, 'modified_on': modified_on,
                                   'user_id': user_id})
        db.session.commit()
        results = {
            "status_code": 200,
            "success": True,
            "message": f"User with id {user_id} has been updated successfully."
        }
    except Exception as e:
        results = {
            "status_code": 500,
            "success": False,
            "message": str(e)
        }
    return jsonify(results)
