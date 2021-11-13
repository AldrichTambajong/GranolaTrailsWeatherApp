# from app import app
# from app import app
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

"""
    Table 1: Users
Columns:
- ID: auto-increment
- email: String
- Password: String

Table 2: User_Attributes
Columns:
- Username: String
- user_state: String
- likes_hiking: boolean
- likes_fishing: boolean
- likes_offroad: boolean
- likes_camping: boolean
- likes_bouldering: boolean

Table 3: Favorites_List
- Username: String
- activity_location: String 

"""
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))
    user_state = db.Column(db.String(80), nullable=False)
    hiking = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    fishing = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    offroad = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    camping = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    bouldering = db.Column(db.Boolean, unique=False, nullable=False, default=False)

    def __repr__(self):
        return f"<Email {self.email}>"

    def get_email(self):
        return self.email


# with app.app_context():
#     db.create_all()
