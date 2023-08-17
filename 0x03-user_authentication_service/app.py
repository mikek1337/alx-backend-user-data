#!/usr/bin/env python3
"""Flask app module"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
app.debug = True
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def hello() -> str:
    """GET /
    Return:
      - JSON payload
    """
    return jsonify({"message": "Bienvenue"})


@app.post('/users', strict_slashes=False)
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
