from flask import Flask, redirect
from werkzeug import secure_filename

UPLOADS_DIRECTORY = 'uploads/'
EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOADS_DIRECTOR'] = UPLOADS_DIRECTORY
app.config['EXTENSIONS'] = EXTENSIONS

@app.route("/")
def form(request):
    return HTMLResponse(
        """
        <form action="/upload" method="post" enctype="multipart/form-data">
            Select image to upload:
            <input type="file" name="file">
            <input type="submit" value="Upload Image">
        </form>
        Or submit a URL:
        <form action="/classify-url" method="get">
            <input type="url" name="url">
            <input type="submit" value="Fetch and analyze image">
        </form>
    """)
