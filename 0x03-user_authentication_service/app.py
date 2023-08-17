#!/usr/bin/env python3
"""Flask app module"""
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def hello() -> str:
    """GET /
    Return:
      - JSON payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """POST /users
    registers new users
    return:
      json payload
    """
    email = request.form['email']
    password = request.form['password']
    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": new_user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "user already exists"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """POST /sessions
    login user
    return:
      json payload"""
    email = request.form['email']
    password = request.form['password']
    user_exists = AUTH.valid_login(email, password)
    if user_exists:
        session_id = AUTH.create_session(email)
        app.config["session_id"] = session_id
        return jsonify({"email": email, "message": "logged in"})
    else:
        return abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
