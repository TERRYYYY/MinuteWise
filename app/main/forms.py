from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo,
from wtforms import ValidationError
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from email_validator import validate_email, EmailNotValidError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category = StringField('Pitch Category',validators=[Required()])
    description = TextAreaField('Pitch Description')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment', validators=[Required()])
    submit = SubmitField('Comment')
