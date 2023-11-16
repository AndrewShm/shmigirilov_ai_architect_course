from pathlib import Path
import os
from werkzeug.utils import secure_filename # самая первая ошибка: cannot import name 'secure_filename' from 'werkzeug'

import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request
from keras.preprocessing.image import ImageDataGenerator

import shutil

try:
    Path('./uploaded').mkdir()
    Path('./uploaded/image').mkdir()
except:
	pass

model = tf.keras.models.load_model('best_model.h5')
app = Flask(__name__)


@app.route('/')
def upload_f():
    return render_template('upload.html')


def finds():
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    test_dir = str(Path('./uploaded/image').resolve())
    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(300, 300),
        color_mode="rgb",
        shuffle=False,
        class_mode='binary',
        batch_size=1)

    pred = model.predict_generator(test_generator)
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
        f.save(str(Path(f'./uploaded/image/{secure_filename(f.filename)}').resolve()))
        val = finds()
        return render_template('pred.html', ss=val)


if __name__ == '__main__':
    app.run(debug=True)
