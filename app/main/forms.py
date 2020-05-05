# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')

class PitchForm(FlaskForm):

 title = StringField('Review title',validators=[Required()])

 review = TextAreaField('Pitch Description')

 submit = SubmitField('Submit')