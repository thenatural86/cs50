from flask import Flask, render_template, request
import random

app = Flask(__name__)

# routes


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def hello():
    # input field to get info from
    name = request.args.get("name")
    if not name:
        return render_template("failure.html")
    return render_template("hello.html", name=name)
