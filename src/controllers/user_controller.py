
from flask import render_template, request, redirect, url_for
import requests

from config import API_URL


def get_list():
    response = requests.get(url=f"{API_URL}/api/user_list/")
    res = response.json()
    if res['success']:
        users = res['data']['userList']
        headers = res['data']['headerList']
        return render_template('pages/user.html', users=users, headers=headers)
    else:
        return res['message']


def add_user_form():
    return render_template('pages/insertUser.html')


def inser_user():

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
    response = requests.post(url=f"{API_URL}/api/user_add/", json=data)
    res = response.json()

    if res["success"]:
        return redirect(url_for('user_routes.get_list'))
    else:
        return res["message"]
