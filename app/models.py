from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime
from flask import abort, session
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    '''
    Model class/db table for the user
    Args:
        db.Model: Connect our class to the database
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True, index=True)
    profile_pic = db.Column(db.String(200), default='profile.png')
    pass_secure = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, default=False)
    comment = db.relationship('Comments', backref='user', lazy='dynamic')

    @property
    def password(self):
        '''
        Define property object to make limit access to pass_secure
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def save_user(self):
        '''
        Function to save a user
        '''
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profile_pic}')"


class Posts(db.Model):
    '''
    Model class/db table for the post made by the writer
    Args:
        db.Model: Connect our class to the database
    '''
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    comments = db.relationship('Comments', backref='comment', lazy='dynamic')
    views = db.Column(db.Integer, default=0)
    

    

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Posts('{self.title}','{self.date_posted}')"

class Comments(db.Model):
    __tablename__ = 'comments' 
    
    id = db.Column(db.Integer, primary_key = True)
    comments = db.Column(db.Text(),nullable=False)
    title = db.Column(db.String(),nullable=False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,blog_id):
        comments = Comments.query.filter_by(posts_id=posts_id).all()

        return comments
        
    def __repr__(self):
        return f'Comment{self.comments}'


class Controller(ModelView):
    def is_accessible(self):
        if current_user.is_admin == True:
            return current_user.is_authenticated
        else:
            abort(404)    
    def not_auth(self):
        return "you are not authorised"

admin.add_view(Controller(Posts, db.session))
