import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet, configure_uploads

from config import config_options

simple = SimpleMDE()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db= SQLAlchemy()
mail = Mail()

bootstrap = Bootstrap()
photos = UploadSet("photos",IMAGES)
def create_app(config_name):
    app = Flask (__name__)
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    app.config["UPLOADED_PHOTOS_DEST"] = "static/img"
    app.config["SECRET_KEY"] = os.urandom(24)
    configure_uploads(app,photos)
    simple.init_app(app)    
        

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
    from.main import main as main_Blueprint
    app.register_blueprint(main_Blueprint)


    return app
