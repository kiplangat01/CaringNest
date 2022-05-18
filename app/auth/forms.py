from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo

from ..models import User
from wtforms import ValidationError

#Registration Form

class RegistrationForm(FlaskForm): 
  email = StringField('Enter your email address',validators=[Required(),Email()])
  username = StringField('Enter your preffered username',validators = [Required()])
  password = PasswordField('Password',validators = [Required(), EqualTo('confirm_password',message = 'Passwords must match')])
  confirm_password = PasswordField('Confirm Password',validators = [Required(),Length(min=8,max=20)])
  submit = SubmitField('Sign Up')


#Validating the user email
  def validate_user_email(self,data_field): #making sure an email address is used once
    if User.query.filter_by(user_email = data_field.data).first(): 
      raise ValidationError('There is an account already created with that email.')

class LoginForm(FlaskForm):
  email = StringField('Enter your Email Address',validators=[Required(),Email()])
  password = PasswordField('Password',validators =[Required()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Login')




