from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from config import config_options
from flask_migrate import Migrate
bootstrap = Bootstrap5()
migrate = Migrate()




db = SQLAlchemy()