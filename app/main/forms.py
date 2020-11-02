from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required
    
class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('submit')