# app.py

from flask import Flask, render_template, request
import os
from model.predict import preprocess_and_predict
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    image_path = None
    result_img_path = None

    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(image_path)

            prediction, result_img_path = preprocess_and_predict(image_path)

    return render_template('index.html', prediction=prediction, 
                           image_path=image_path, result_img_path=result_img_path)

if __name__ == '__main__':
    app.run(debug=True)
