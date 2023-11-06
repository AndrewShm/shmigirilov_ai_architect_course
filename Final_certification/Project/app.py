import os
from werkzeug import secure_filename # самая первая ошибка: cannot import name 'secure_filename' from 'werkzeug'

import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request
from keras.preprocessing.image import ImageDataGenerator

import shutil

try:
    shutil.rmtree('/uploaded/image')
    % cd uploaded % mkdir image % cd .. # строка, которая вызывает ошибку синтаксиса (при коммите строки 2 и редактировании строки 54)
	print()
except:
	pass

model = tf.keras.models.load_model('best_model.h5')
app = Flask(__name__)

UPLOAD_FOLDER = '/uploaded/image'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def upload_f():
    return render_template('upload.html')


def finds():
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    test_dir = UPLOAD_FOLDER
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


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))) # строка, на которой возникает ошибка пути, после того как закомитил строки 12 и 13
        val = finds()
        return render_template('pred.html', ss=val)


if __name__ == '__main__':
    app.run(debug=True)
