from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, StringField, SubmitField,
                     ValidationError)
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Donor

#Registration Form

class RegistrationForm(FlaskForm): 
  email = StringField('Enter your email address',validators=[DataRequired(),Email()])
  username = StringField('Enter your preffered username',validators = [DataRequired()])
  password = PasswordField('Password',validators = [DataRequired(), EqualTo('confirm_password',message = 'Passwords must match')])
  confirm_password = PasswordField('Confirm Password',validators = [DataRequired()])
  submit = SubmitField('Sign Up')


#Validating the user email
  def validate_user_email(self,data_field): #making sure an email address is used once
    if Donor.query.filter_by(user_email = data_field.data).first(): 
      raise ValidationError('There is an account already created with that email.')

class LoginForm(FlaskForm):
  email = StringField('Enter your Email Address',validators=[DataRequired(),Email()])
  password = PasswordField('Password',validators =[DataRequired()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Login')




