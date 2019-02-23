from flask import Flask, redirect
from werkzeug import secure_filename

UPLOADS_DIRECTORY = 'uploads/'
EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOADS_DIRECTOR'] = UPLOADS_DIRECTORY
app.config['EXTENSIONS'] = EXTENSIONS

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
