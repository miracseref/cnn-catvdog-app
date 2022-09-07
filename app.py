from crypt import methods
import tensorflow as tf
from tensorflow import keras
from flask import Flask, request, app, jsonify, url_for, render_template

app = Flask(__name__)

# Load the model 
model = tf.keras.models.load_model('model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    pass

@app.route('/predict', methods=['POST'])
def predict():
    pass

if __name__ == "__main__":
    app.run(debug=True)