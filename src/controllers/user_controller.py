from flask import render_template, request, redirect, url_for
import requests

from config import API_URL


def get_list():
    response = requests.get(url=f"{API_URL}/api/user_list_1/")
    res = response.json()
    if res['success']:
        users = res['data']['userList']
        headers = res['data']['headerList']
        return render_template('pages/user.html', users=users, headers=headers)
    else:
        return res['message']


def add_user_form():
    is_update = False
    return render_template('pages/editUser.html', is_update=is_update)


def insert_user():
    data = {
        'username': request.form['username'],
        'full_name': request.form['full_name'],
        'email': request.form['email'],
        'phone_number': request.form['phone_number'],
        'report_access': True if request.form.get('report_access') == "" else False,
        'view_costs': True if request.form.get('view_costs') == "" else False,
        'enabled': True if request.form.get('enabled') == "" else False,
        'is_corporated': True if request.form.get('is_corporated') == "" else False,
        'last_login_date': request.form['last_login_date'],
        'created_on': request.form['created_on'],
        'modified_on': request.form['modified_on']
    }
    response = requests.post(url=f"{API_URL}/api/user_add_1/", json=data)
    res = response.json()

    if res["success"]:
        return redirect(url_for('user_routes.get_list'))
    else:
        return res["message"]


def update_user_form(user_id):
    is_update = True
    response = requests.get(url=f"{API_URL}/api/user_1/{user_id}").json()
    if response["success"]:
        user = response["data"]
        return render_template('pages/editUser.html', is_update=is_update, user=user)
    else:
        return response["message"]


def update_user(user_id):
    data = {
        'username': request.form['username'],
        'full_name': request.form['full_name'],
        'email': request.form['email'],
        'phone_number': request.form['phone_number'],
        'report_access': True if request.form.get('report_access') == "" else False,
        'view_costs': True if request.form.get('view_costs') == "" else False,
        'enabled': True if request.form.get('enabled') == "" else False,
        'is_corporated': True if request.form.get('is_corporated') == "" else False,
        'last_login_date': request.form['last_login_date'],
        'created_on': request.form['created_on'],
        'modified_on': request.form['modified_on']
    }
    response = requests.post(
        url=f"{API_URL}/api/user_update_1/{user_id}", json=data)
    res = response.json()

    if res["success"]:
        return redirect(url_for('user_routes.get_list'))
    else:
        return res["message"]
