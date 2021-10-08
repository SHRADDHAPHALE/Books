import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_dance.contrib.google import make_google_blueprint
from flask_login import LoginManager

app = Flask(__name__)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'

blueprint = make_google_blueprint(client_id="522141288574-7ir7qd4f61de0ghch8fp6hv9hormpnng.apps.googleusercontent.com",
    client_secret="JEBf0q41M3qEOj4TznIAz5LP",offline=True,
    scope=["profile", "email"])

app.config["SECRET_KEY"] = "mysecretkey"
basedir = os.path.abspath(os.path.dirname(__file__))
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

app.register_blueprint(blueprint, url_prefix="/login")
