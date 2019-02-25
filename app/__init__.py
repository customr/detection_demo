import os
from flask import Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from wtforms import SubmitField


app = Flask(__name__, template_folder='templates', static_folder='static')

DIR = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(DIR, 'data/')
UPLOAD_FOLDER = os.path.join(DIR, 'uploads/')
SAVE_FOLDER = os.path.join(DIR, 'results/')

if not os.path.isdir(DIR):
	os.mkdir(DIR)

if not os.path.isdir(UPLOAD_FOLDER):
	os.mkdir(UPLOAD_FOLDER)

if not os.path.isdir(SAVE_FOLDER):
	os.mkdir(SAVE_FOLDER)

app.config['SECRET_KEY'] = 'you_never_guess'
app.config['SAVE_FOLDER'] = SAVE_FOLDER
app.config['UPLOADED_PHOTOS_DEST'] = UPLOAD_FOLDER

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')])
    submit = SubmitField(u'Upload')


from app import routes
