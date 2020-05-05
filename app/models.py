from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'pitch',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'




























# class Pitch:

#     all_pitches = []

#     def __init__(self,movie_id,title,imageurl,review):
#         self.movie_id = movie_id
#         self.title = title
#         self.imageurl = imageurl
#         self.review = review


#     def save_pitch(self):
#         Review.all_pitches.append(self)


#     @classmethod
#     def clear_pitch(cls):
#         Pitch.all_pitches.clear()

#     @classmethod
#     def get_pitch(cls,id):

#         response = []

#         for pitch in cls.all_pitches:
#             if pitch.movie_id == id:
#                 response.append(review)

#         return response