from flask import render_template, Blueprint

main = Blueprint("main", __name__)

@main.get("/")
def index():
    return render_template("index.html")