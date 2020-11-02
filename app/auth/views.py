from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import User
from .forms import RegistrationForm,LoginForm,adminForm
from .. import db
from flask_login import login_user,logout_user,login_required


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    title = "Registration"
    return render_template('auth/register.html', form = form, title = title)

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/admin',methods=['GET','POST'])
@role_required
def create_admin():
    admin_form = adminForm()

    if request.method == "POST":
        new_user = User(username = request.form['username'], email = request.form['email'], password = request.form['password'], is_admin=True)
        db.session.add(new_user)
        db.session.commit()
        return "you have created an admin account"
       

    title = "login"
    return render_template('auth/admin.html',admin_form = admin_form,title=title)
    

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))