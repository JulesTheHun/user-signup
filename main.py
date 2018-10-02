from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

def basic_validate(info):
    valid = False
    has_space = False

    for char in info:
        if char == " ":
            has_space = True
            break

    if len(info) >= 3 and len(info) <= 20 and not(has_space):
        valid = True
    return valid

def email_validate(email):
    if email == "":
        return True
    valid = False
    has_space = False
    has_period = False
    has_at = False

    for char in email:
        if char == " ":
            has_space = True
            break
        if char == ".":
            has_period = True
        if char == "@":
            has_at = True

    if len(email) >= 3 and len(email) <= 20 and not(has_space) and has_period and has_at:
        valid = True
    return valid

def match_validate(password1, password2):
    match = False
    if password1 == password2:
        match = True
    return match

@app.route("/welcome", methods=['POST'])
def welcome():
    name_error = True
    password_error = True
    match_error = True
    email_error = True

    username = request.form['username']
    password1 = request.form['password1']
    password2 = request.form['password2']   
    email = request.form['email']

    if basic_validate(username):
        name_error = False
    else:
        username = ""
    if basic_validate(password1):
        password_error = False
    if match_validate(password1, password2):
        match_error = False
    if email_validate(email):
        email_error = False

    if name_error or password_error or match_error or email_error:
        return redirect("/", username=username, name_error=name_error, password_error=password_error, match_error=match_error, email_error=email_error)

    return render_template("welcome.html", username=username)

@app.route("/")
def index():
    return render_template("index.html")

app.run()