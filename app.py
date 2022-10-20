from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/about")
def about_me():
    return render_template("about_me.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")