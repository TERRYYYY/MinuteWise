from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitchescategory = db.relationship('Pitchcategory',backref = 'user',lazy = "dynamic")

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
    users = db.relationship('User',backref = 'pitch',lazy="dynamic")
    

    def __repr__(self):
        return f'User {self.name}'


class Pitchcategory:

    __tablename__ = 'pitchescategory'

    id = db.Column(db.Integer,primary_key = True)
    pitches_id = db.Column(db.Integer)
    piches_title = db.Column(db.String)
    pitches_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_pitchescategory(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitchescategory(cls,id):
        pitchescategory = Pitch.query.filter_by(pitch_id=id).all()
        return pitchescategory