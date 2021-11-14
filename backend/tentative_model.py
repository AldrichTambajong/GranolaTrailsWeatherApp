from app import app
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
db = SQLAlchemy(app)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

    def __repr__(self):
        return f"<User {self.username}>"
    
    def get_email(self):
        return self.email
    
  #  def get_password(self):
    #    return self.password


class User_Attributes(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    user_state = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    hiking = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    fishing = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    offroad = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    camping = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    bouldering = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    def __repr__(self):
       return f"<State: {self.user_state}>"

class Favorites_list(db.Model):
    username = db.Column(db.String(80), nullable=False)
    activity_location = db.Column(db.String(80), nullable=False)
    # Maybe place activity names too or
    # use boolean values as for the attributes
    # location just feels incomplete
db.create_all()
