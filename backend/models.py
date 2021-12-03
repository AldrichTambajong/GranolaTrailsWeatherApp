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

# from app import app
# from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """
    id: int
        primary key, automatically generated
    email: str
        valid email, must be unique
    password: str
        hashed
    user_state: str
        2-character state code
    hiking: bool
    fishing: bool
    offroad: bool
    camping: bool
    bouldering: bool
        true if the user is interested in that activity
        false if not
    """

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
        """
        returns the email for the user
        """
        return self.email

    def get_state(self):
        """
        returns the state for the user
        """
        return self.user_state

    def get_favorites(self):
        """
        returns a list of the user's favorite activities
        """
        activities = []
        if self.hiking:
            activities.append("hiking")
        if self.fishing:
            activities.append("fishing")
        if self.offroad:
            activities.append("auto_and_atv")
        if self.camping:
            activities.append("camping")
        if self.bouldering:
            activities.append("canyoneering")
        return activities


# with app.app_context():
#     db.create_all()
