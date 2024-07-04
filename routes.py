from flask import request, render_template, current_app as app
import numpy as np
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename
import os
import cv2

model = load_model('models/ancer_detector.h5')

def preprocess_image(image_path, target_size):
    image = cv2.imread(image_path)
    image = cv2.resize(image, target_size)
    image = image / 255.0
    return image

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        image = preprocess_image(filepath, (128, 128))
        prediction = model.predict(np.expand_dims(image, axis=0))

        return f'Prediction: {"Cancerous" if prediction[0] > 0.2 else "Non-cancerous"}'

    return render_template('upload.html')

#%%
