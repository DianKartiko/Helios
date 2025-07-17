from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

pages = Blueprint("main", __name__, template_folder="templates")

@pages.route('/')
def index():
    try:
        return render_template("index.html")
    except TemplateNotFound:
        abort(404)
