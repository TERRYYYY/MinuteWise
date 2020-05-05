import unittest
from app.models import Pitch ,User
from app import db 
Pitch = Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_pitch = Review(pitch_id=12345,pitch_title='Review for movies',pitches_review='This movie is the best thing since sliced bread',user = self.user_James )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

    def tearDown(self):
        Pitchcategory.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_id,12345)
        self.assertEquals(self.new_pitch.pitch_title,'Review for movies')
        self.assertEquals(self.new_pitch.pitch_review,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_pitch.user,self.user_James)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitchcategory.query.all())>0)

    def test_get_pitch_by_id(self):

        self.new_pitch.save_pitch()
        got_pitch = Pitchcategory.get_pitch(12345)
        self.assertTrue(len(got_pitch) == 1)