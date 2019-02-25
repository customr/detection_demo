import os
from flask import render_template, send_from_directory
from app import app, UploadForm, photos
from app.src.yolov3.detect import main as detect


@app.route('/', methods=['GET', 'POST'])
def index():
	form = UploadForm()
	result = None

	if form.validate_on_submit():
		filename = photos.save(form.photo.data)
		result = detect(
			path_to_input_image=app.config['UPLOADED_PHOTOS_DEST']+filename, 
			save_as=app.config['SAVE_FOLDER']+filename
			)

	return render_template('index.html', form=form, result=result)


@app.route(app.config['SAVE_FOLDER'] + '<path:filename>')
def upload(filename):
	return send_from_directory(app.config['SAVE_FOLDER'], filename)
