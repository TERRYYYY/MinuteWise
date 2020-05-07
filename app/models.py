from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get((user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    # email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitch_id = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comment' , backref = 'user', lazy = 'dynamic')

    def __init__(self,email,username,password_hash,bio,profile_pic_path):
        self.email = email
        self.username = username
        self.password_hash = password_hash
        self.bio = bio
        self.profile_pic_path = profile_pic_path



    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    user_id = db.Column(db.Integer , db.ForeignKey('users.id'))
    # users = db.relationship('User',backref = 'pitch',lazy="dynamic")
    category = db.Column(db.String(255), index = True)
    description = db.Column(db.String(255), index = True)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    comments = db.relationship('Comment' , backref = 'pitch', lazy = 'dynamic')

    def save_pitch(self):
        def save_review(self):
            db.session.add(self)
            db.session.commit()

    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.all()
        return pitches

    def __repr__(self):
        return f'User {self.name}'

class Comment(db.Model):
    __tablename__= 'comments'
    id = db.Column(db.Integer,primary_key = True)
    description = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))