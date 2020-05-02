from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Pitchtitle',validators=[Required()])
    review = TextAreaField('Pitch review', validators=[Required()])
    submit = SubmitField('Submit')