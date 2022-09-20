import os

from flask import Flask, app, flash, redirect, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array, load_img
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/files'
SECRET_KEY = 'supersecretkey'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY

# Load the model
model = load_model('model.h5')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


def preprocess_image(img):
    img = load_img(img, target_size=(200, 200))
    img = img_to_array(img)
    img = img.reshape(1, 200, 200, 3)
    return img


@app.route('/', methods=['GET', 'POST'])
def predict():
    # upload_file()
    # if os.path.isfile(app.config['UPLOAD_FOLDER']):    
    #     for file in os.listdir(app.config['UPLOAD_FOLDER']):
    #         if (file.endswith(".png") or file.endswith(".jpg")
    #                 or file.endswith(".jpeg")):
    #             image_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
    # if 'image_path' in locals():
    #     input_arr = preprocess_image(image_path)
    #     prediction = model.predict(input_arr)
    # if 'prediction' in locals():
    #     if prediction[0][0] == 0:
    #         prediction_text = 'This is a cat.'
    #     else:
    #         prediction_text = 'This is a dog.'
    #     os.remove(image_path)
    #     return render_template('index.html',
    #                            prediction_text=prediction_text)
    # else:
    #     if 'image_path' in locals():
    #         os.remove(image_path)
    #     return render_template('index.html')
    return render_template('index.html')


# if __name__ == "__main__":
app.run(debug=True)
