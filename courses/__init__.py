import os
from flask import Flask,Blueprint,render_template
from flask_restful import Resource,Api
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import secure_filename
from flask_cors import CORS
import secrets
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required,JWTManager
import datetime






main = Blueprint('main',__name__)
UPLOAD_FOLDER = '/static'
ALLOWED_EXTENSIONS = set(['.png','.jpg','.jpeg'])




app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})




api = Api(app)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = os.environ.get('FLASk_APP_KEY','sample key')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=60)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///course.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

from courses.route import *

def save_imge(photo,default_photo):
    if photo!=None:
        hash_photo = secrets.token_urlsafe(10)
        _,file_extention = os.path.splitext(photo.filename)
        if file_extention in ALLOWED_EXTENSIONS:
            photo_name  = hash_photo + file_extention
            file_path = os.path.join(app.root_path,'static/img',photo_name)
            photo.save(file_path)
            return photo_name
        else:
            return default_photo
    else:
        return default_photo
    
