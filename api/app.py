from flask import Flask, redirect, render_template, request, url_for
from werkzeug import secure_filename
from fastai.vision import load_learner, open_image
import os


# folder for uploads save
UPLOADS_DIRECTORY = 'static/uploads'
# valid extension
EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOADS_DIRECTORY'] = UPLOADS_DIRECTORY
app.config['EXTENSIONS'] = EXTENSIONS

classes = ['fico', 'kiska']

# load model
model = load_learner('./models')

# main route
@app.route('/')
def index():
    return render_template('index.html')

def check_if_valid(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    # check if valid
    if file and check_if_valid(file.filename):
        # make the filename to be a secure version of it.
        filename = secure_filename(file.filename)
        # save image to directory
        save_to=os.path.join(app.config['UPLOADS_DIRECTORY'], filename)
        file.save(save_to)
        # make prediction
        prediction,_,_ = model.predict(open_image(save_to))
        return redirect(url_for('classification', result=prediction))

@app.route('/classification/<result>')
def classification(result):
    return render_template('result.html', result=result)

if __name__ == '__main__':
   port = int(os.environ.get('PORT', 5000))
   app.run(host='0.0.0.0')
