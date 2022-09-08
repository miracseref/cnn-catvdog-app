import numpy as np
import matplotlib.pyplot as plt
from crypt import methods
import tensorflow as tf
from tensorflow import keras
from flask import Flask, request, app, jsonify, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/images'

# Load the model 
model = tf.keras.models.load_model('model.h5')

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField('Upload File')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                app.config['UPLOAD_FOLDER'],
                                secure_filename(file.filename))) # Then save the file
        return "File has been uploaded."
    return render_template('index.html', form=form)

@app.route('/predict', methods=['POST'])
def predict():
    # TROUVE LE CHEMIN POUR L'IMAGE AVEC LE MODULE OS 
    # ENSUITE CORRIGE LA 1ERE VARIABLE CI-DESSOUS
    image_path = os.path.abspath(app.config['UPLOAD_FOLDER'])
    image = tf.keras.preprocessing.image.load_img(image_path)
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) # convert single image to batch
    predictions = model.predict(input_arr)
    os.remove(image_path)
    return render_template('index.html', predict_text= f"This is a {predictions}")

if __name__ == "__main__":
    app.run(debug=True)