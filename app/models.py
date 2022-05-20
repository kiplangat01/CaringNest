from datetime import datetime
from urllib import request

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return Donor.query.get(int(user_id))


class Donor(UserMixin,db.Model):
    __tablename__ = 'donor'
    
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    age = db.Column(db.String())
    contact = db.Column(db.String())
    weight = db.Column(db.String()) 
    blood_type = db.Column(db.String())
    donate_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    # save donors
    def save_Donor(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_Donors(cls):
        Donors = Donor.query.all()
        return Donors

    
     # securing passwords
    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')


    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'
    
    
class Doctor(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    department = db.Column(db.String(255))
    contact = db.Column(db.String())
    request_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    
     # securing passwords
    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')


    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'
    
    
