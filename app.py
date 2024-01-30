from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

from helpers import register_user, login_user, is_admin

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    # def read_qr_code(filename):
    # """Read an image and read the QR code.
    
    # Args:
    #     filename (string): Path to file
    
    # Returns:
    #     qr (string): Value from QR code
    # """
    
    # try:
    #     img = cv2.imread(filename)
    #     detect = cv2.QRCodeDetector()
    #     value, points, straight_qrcode = detect.detectAndDecode(img)
    #     return value
    # except:
    #     return
        
    return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password_confirmation = request.form.get("confirmation")

        if register_user(username, password, password_confirmation):
            session["username"] = "username1" # currently a dummy value
            return redirect("/")
        else:
            return render_template('register.html', error_hit=True)

    else:
        return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if login_user(username, password):
            session["username"] = username
            return redirect("/")
        else:
            return render_template('login.html', error_hit=True)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()

    return render_template('index.html')      