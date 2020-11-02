from flask import render_template, redirect, url_for,abort,request,flash
from . import main
from ..models import Posts, User, Comments
from .forms import CommentsForm
from ..requests import get_quotes
from flask_login import current_user,login_required
import sqlalchemy


@main.route('/')
def index():
    posts = Posts.query.all()
    quotes = get_quotes()
    return render_template('index.html', posts=posts, quote=quotes)


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
    posts = Posts.query.all()
    return render_template('blogs.html', posts=posts)

@main.route('/comments/<int:posts_id>', methods=['GET','POST'])
@login_required
def new_comment(posts_id):
    form = CommentsForm()
    posts = Posts.query.get(posts_id)
    comment = Comments.query.filter_by(post_id=posts_id).all()
    if form.validate_on_submit():
        comments = form.comment.data
        
        post_id = posts_id
        user_id = current_user._get_current_object().id
        new_comment= Comments(comments=comments,posts_id=post_id, user_id=user_id)
        new_comment.save_comment()      
       
        return redirect(url_for('main.new_comment', posts_id=post_id))
    
    return render_template('comments.html', form=form, comment=comment, posts_id=post_id,posts=posts)

