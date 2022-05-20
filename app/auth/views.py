from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from .. import db
from ..models import Doctor, Donor
from . import auth
from .forms import LoginForm, RegistrationForm


#View functions
#Login route
@auth.route('/login',methods=['GET','POST'])
def login(): 
  '''Function that renders the login template'''
  login_form = LoginForm()
  if login_form.validate_on_submit(): 
    user = Donor.query.filter_by(user_email = login_form.email.data).first()
    if user is not None and user.verify_password(login_form.password.data): #confirms existence of a user
      login_user(user,login_form.remember.data)
      return redirect(request.args.get('next') or url_for('main.index'))
    
    flash('You have been logged in!')
  
  title = "Application login"
  return render_template('auth/login.html',login_form = login_form,title = title)

#Registration route
@auth.route('/register',methods = ["GET","POST"])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = Donor(user_email = form.email.data, username = form.username.data,password = form.password.data)
    db.session.add(user)
    db.session.commit()
    
    flash(f'Account created for {user.username}!')
    
    return redirect(url_for('auth.login'))
    title = "New User Account"
  return render_template('auth/register.html',form = form)

#Logout route
@auth.route('/logout')
@login_required
def logout(): 
  logout_user()
  return redirect(url_for("main.index"))