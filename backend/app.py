"""
    creates the app
"""

import os
from flask import Flask, request, session
from flask.json import jsonify
from dotenv import load_dotenv, find_dotenv

# from flask_login import current_user, LoginManager, login_user, logout_user
# from sqlalchemy import func
from passlib.hash import sha256_crypt
from models import db, User

from national_parks import get_parks_and_weather

app = Flask(__name__)

db.init_app(app)

load_dotenv(find_dotenv())

# login_manager = LoginManager()

db_url = os.getenv("DATABASE_URL")
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "SET_A_SECRET_KEY")


@app.route("/login", methods=["POST"])
def login():
    session.pop("favorites", default=None)
    session.pop("state", default=None)
    data = request.get_json()
    user = User.query.filter_by(email=data.get("email")).first()

    jsonData = {"status": "invalid"}
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
            session["favorites"] = user.get_favorites()
            session["state"] = user.get_state()
    return jsonify(jsonData)


@app.route("/logout", methods=["POST"])
def logout():
    """
    logs the current user out
    clears the session storage
    """
    session.pop("favorites", default=None)
    session.pop("state", default=None)
    json_data = {"status": 200}
    return jsonify(json_data)


@app.route("/signUp", methods=["POST"])
def signUp():
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
    """
    returns a sample of parks in ther user's state that feature the activities they like
    """
    # data = request.get_json()
    user_state = session["state"]
    favorites = session["favorites"]
    parks = get_parks_and_weather(favorites, user_state)
    return jsonify(parks)


def main():
    """
    runs the app
    """
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))


if __name__ == "__main__":
    main()
