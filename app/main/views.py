from flask import render_template, redirect, url_for,abort
from . import main
from ..models import Posts, User
from flask_login import current_user
import sqlalchemy


@main.route('/')
def index():
    posts = Posts.query.all()
    return render_template('index.html', posts=posts)


@main.route('/posts/<string:slug>')
def posts(slug):
   try:
    post = Posts.query.filter_by(slug=slug).one()
    return render_template('posts.html', post=post)
   except sqlalchemy.orm.exc.NoResultFound:
        abort(404)

@main.route('/account')
def account():
    return render_template('account.html')

@main.route('/blogs')
def blogs():
    return render_template('blogs.html')