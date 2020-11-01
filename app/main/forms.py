from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required
from flask_wtf.file import FileField
from ..models import Posts

class PostsForm(FlaskForm):
    """
    post form to create new posts
    """
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Blog Content', validators=[Required()])
    image = FileField('Blog Image')
    submit = SubmitField('Post Blog')
