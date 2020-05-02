class Pitch:

    all_pitches = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_pitch(self):
        Review.all_pitches.append(self)


    @classmethod
    def clear_pitch(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitch(cls,id):

        response = []

        for pitch in cls.all_pitches:
            if pitch.movie_id == id:
                response.append(review)

        return response