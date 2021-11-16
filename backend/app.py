"""
    creates the app
"""

import os
from flask import json, Flask, request
from flask.json import jsonify
from dotenv import load_dotenv, find_dotenv
from flask_login import current_user, LoginManager, login_user, logout_user
from sqlalchemy import func
from passlib.hash import sha256_crypt
from tentative_model import *

from national_parks import get_parks_and_weather

app = Flask(__name__)

db.init_app(app)

load_dotenv(find_dotenv())

login_manager = LoginManager()

db_url = os.getenv("DATABASE_URL")
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/login", methods=["POST"])
def login():

    if request.method == "POST":
        data = request.get_json()
        user = User.query.filter_by(email=data.get("email")).first()

        if user:
            password = sha256_crypt.verify(data.get("password"), user.password)

            if password:
                jsonData = {
                    "email": data.get("email"),
                    "password": data.get("password"),
                    "user_state": user.user_state,
                    "login": "valid",
                    "status": 200,
                }
            else:
                jsonData = {"status": "invalid"}
            return jsonify(jsonData)


@app.route("/signUp", methods=["POST"])
def signUp():
    if request.method == "POST":
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        user_state = data.get("user_state")
        hiking = data.get("hiking")
        fishing = data.get("fishing")
        offroad = data.get("offroad")
        camping = data.get("camping")
        bouldering = data.get("bouldering")

        if User.query.filter_by(email=email).first():
            errorObj = {"message": "Email already exists!", "status": 300}
            return jsonify(errorObj)

        password = sha256_crypt.encrypt(password)

        new_account = User(
            email=email,
            password=password,
            user_state=user_state,
            hiking=hiking,
            fishing=fishing,
            offroad=offroad,
            camping=camping,
            bouldering=bouldering,
        )
        db.session.add(new_account)
        db.session.commit()
        successObj = {"message": "New user registered", "status": 200}
        return jsonify(successObj)


@app.route("/parks", methods=["POST"])
def get_users_parks():
    data = request.get_json()
    user_state = data.get("user_state")
    # user_state = "UT"
    favorites = [
        "fishing",
        "hiking",
        "camping",
    ]
    parks = get_parks_and_weather(favorites, user_state)
    return jsonify(parks)


def main():
    """
    runs the app
    """
    app.run(
        debug=True,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8081)),
    )


if __name__ == "__main__":
    main()
