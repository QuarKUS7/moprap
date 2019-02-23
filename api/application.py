from flask import Flask, redirect
from werkzeug import secure_filename
from fastai.vision import (
    ImageDataBunch,
    ConvLearner,
    open_image,
    get_transforms,
    models,
)

UPLOADS_DIRECTORY = 'uploads/'
EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOADS_DIRECTOR'] = UPLOADS_DIRECTORY
app.config['EXTENSIONS'] = EXTENSIONS

# load model
classes = ['fico', 'kiska']

data = ImageDataBunch.from_name_re(
    image_path,
    ds_tfms=get_transforms(),
    size=224
)

model = create_cnn(data, models.resnet34, metrics=error_rate)
model.load_learner("/models/export.pkl")

# main route
@app.route('/')
def index():
    return render_template('index.html')

def check_if_allowed(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['EXTENSIONS']

@app.rout('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and check_if_allowed(file.filename):
        filename = secure_filename(file.filename)
        save_to=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_to)
        prediction = model.predict(save_to)
        return redirect(url_for('classification', result=predict))

@app.route('/classification/<result>')
def classification(result):
    return render_template('result.html', result=result)

if __name__ == '__main__':
   app.run(debug=True)
