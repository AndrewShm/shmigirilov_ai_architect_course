from pathlib import Path
import os
from werkzeug.utils import secure_filename

import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image

import shutil

shutil.rmtree('uploaded')
Path('./uploaded').mkdir()
Path('./uploaded/image').mkdir()

model = tf.keras.models.load_model('best_model.h5')


app = Flask(__name__)


@app.route('/')
def upload_f():
    return render_template('upload.html')


@app.route('/faqs')
def faqs():
    return render_template('faqs.html')


@app.route('/about')
def about():
    return render_template('about.html')


def finds(image_path):
    img = image.load_img(image_path, target_size=(300, 300))
    x = image.img_to_array(img)
    x = x / 255.0
    x = x.reshape((1, 300, 300, 3))
    pred = model.predict(x)

    if pred > 0.5:
        pred_text = 'def_front'
    else:
        pred_text = 'ok_front'
    print(pred)
    return pred_text


@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        image_path = str(Path(f'./uploaded/image/{secure_filename(f.filename)}').resolve())
        f.save(image_path)
        val = finds(image_path)
        return render_template('pred.html', ss=val)


if __name__ == '__main__':
    app.run(debug=True)