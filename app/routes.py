from flask import render_template, Blueprint, request, redirect, url_for, flash
from .services import ai_service

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():

    response = None

    if request.method == "POST":

        notes = request.form.get("notes", "").strip()
        if not notes:
            flash("please enter text in the box to continue", "error")
            return redirect(url_for("main.index"))

        response = ai_service.summarise_clinical_notes(notes=notes)

    return render_template("index.html", response=response)