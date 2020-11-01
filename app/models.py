from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    '''
    Model class/db table for the user
    Args:
        db.Model: Connect our class to the database
    '''
    __tablename__  = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(255), unique = True, index=True)
    pass_secure = db.Column(db.String(200))

    @property
    def password(self):
        '''
        Define property object to make limit access to pass_secure
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save_user(self):
        '''
        Function to save a user
        '''
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profile_pic_path}')"

class Posts(db.Model):
    '''
    Model class/db table for the post made by the writer
    Args:
        db.Model: Connect our class to the database
    '''
    __tablename__  = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(200))
    author = db.Column(db.String(200))
    date_posted = db.Column(db.DateTime)
    slug = db.Column(db.String(200))

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Posts('{self.title}','{self.date_posted}')"


