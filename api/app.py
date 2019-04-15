from flask import Flask, redirect, render_template, request, url_for
from werkzeug import secure_filename
from fastai import *
from fastai.vision import *
import os
from pathlib import Path


# folder for uploads save
UPLOADS_DIRECTORY = 'static/uploads'

app = Flask(__name__)
app.config['UPLOADS_DIRECTORY'] = UPLOADS_DIRECTORY
classes = ['fico', 'kiska']

# load model
path = Path("")
data = ImageDataBunch.single_from_classes(path, classes, tfms=get_transforms(), size=224).normalize(imagenet_stats)
model = create_cnn(data, models.resnet34)
model.load('./fk')

# main route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    # make the filename to be a secure version of it.
    filename = secure_filename(file.filename)
    # save image to directory
    save_to = os.path.join(app.config['UPLOADS_DIRECTORY'], filename)
    file.save(save_to)
    # make prediction
    prediction, _, _ = model.predict(open_image(save_to))
    return redirect(url_for('classification', result=prediction))

@app.route('/classification/<result>')
def classification(result):
    return render_template('result.html', result=result)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
