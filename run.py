"""Thorin flask app python file"""
import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Define route for index page"""
    return render_template("index.html")


@app.route("/about")
def about():
    """Define route for about page"""
    data = []
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():
    """Define route for contact page"""
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    """Define route for careers page"""
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
