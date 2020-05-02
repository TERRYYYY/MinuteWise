class Pitch:

    all_pitches = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_pitch(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_pitch(cls):
        Pitch.all_pitches.clear()