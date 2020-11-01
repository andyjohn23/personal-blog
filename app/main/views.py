from flask import render_template,redirect,url_for
from . import main
from ..models import Posts

@main.route('/')
def index():
    
    return render_template('index.html')

@main.route('/posts/<string:slug>')
def posts(slug):
    post = Posts.query.filter_by(slug=slug).one()
    return render_template('posts.html', post=post)