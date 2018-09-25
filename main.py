from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

def basic_validate(username):
    valid = False
    has_space = True

    for 

    if len(username) >= 3 or len(username) <= 20 and not(has_space):
        valid = True
    return valid

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']

    return render_template("welcome.html", username=username)

@app.route("/")
def index():
    return render_template("index.html")

app.run()