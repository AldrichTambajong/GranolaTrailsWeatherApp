"""
    creates the app
"""

import os
from flask import json, Flask, request
from flask.json import jsonify
from dotenv import load_dotenv, find_dotenv, main
from flask_login import current_user, LoginManager, login_user, logout_user
from sqlalchemy import func
from passlib.hash import sha256_crypt

from national_parks import get_parks_by_activities, find_activity

app = Flask(__name__)

load_dotenv(find_dotenv())

login_manager = LoginManager()


@app.route("/test")
def testing():
    fishing = find_activity("Fishing")
    fishing_id = fishing[0]["id"]
    fishing_parks = get_parks_by_activities(activity_ids=[fishing_id], limit=1)
    weather = json.dumps(fishing_parks[0])
    return weather


@app.route("/login", methods=["POST"])
def login():

    if request.method == "POST":
        #     data = flask.request.get_json()
        #     user = User.query.filter_by(email=data.get("email")).first()
        jsonData = {
            "email": "test",
            "password": "test",
            "name": "test",
            "login": "valid",
            "status": 200,
        }
        return jsonify(jsonData)

    #     if user:
    #         password = sha256_crypt.verify(data.get("password"), user.password)

    #         if password:
    #             jsonData = {
    #                 "email": data.get("email"),
    #                 "password": data.get("password"),
    #                 "name": user.firstName,
    #                 "login": "valid",
    #                 "status": 200,
    #             }
    #             return jsonify(jsonData)
    #         else:
    #             jsonData = {"status": "invalid"}
    #             return flask.jsonify(jsonData)


@app.route("/signUp", methods=["POST"])
def signUp():
    return "boo"
    # if flask.request.method == "POST":
    #     data = flask.request.get_json()
    #     firstName = data.get("firstName")
    #     lastName = data.get("lastName")
    #     email = data.get("email")
    #     password = data.get("password")

    #     if User.query.filter_by(email=email).first():
    #         errorObj = {"message": "Email already exists!", "status": 300}
    #         return jsonify(errorObj)
    #     elif User.query.filter_by(password=password).first():
    #         errorObj = {"message": "Password is already taken", "status": 300}
    #         return jsonify(errorObj)

    #     password = sha256_crypt.encrypt(password)

    #     new_account = User(firstName, lastName, email, password)
    #     db.session.add(new_account)
    #     db.session.commit()
    #     successObj = {"message": "New user registered", "status": 200}
    #     return jsonify(successObj)


def main():
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))


if __name__ == "__main__":
    main()
