from flask import Flask, request, render_template_string
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return """
    <h1>Secure Coding Review Demo</h1>

    <h2>Login</h2>
    <form method="post" action="/login">
        Username: <input name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <button type="submit">Login</button>
    </form>

    <hr>

    <h2>Comment</h2>
    <form action="/comment">
        <input name="msg">
        <button type="submit">Submit</button>
    </form>

    <hr>

    <h2>Upload File</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
    """

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    return f"Welcome {username}"

@app.route("/comment")
def comment():
    msg = request.args.get("msg", "")
    return render_template_string(
        "<h3>User Comment</h3><p>{{msg}}</p>",
        msg=msg
    )

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if not file:
        return "No file selected"

    filename = secure_filename(file.filename)

    file.save(os.path.join(UPLOAD_FOLDER, filename))

    return "Upload Successful"

if __name__ == "__main__":
    app.run()
