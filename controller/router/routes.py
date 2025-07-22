from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

page = Blueprint("main", __name__, template_folder='templates')

@page.route('/')
def index():
    try: 
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@page.route('/updating')
def update():
    return render_template('src/update.html')

@page.route('/exotic/')
def exotic():
    return render_template('src/project/exotic.html')

@page.route('/linear/')
def linear():
    return render_template('src/project/linear.html')

@page.route('/nest/')
def nest():
    return render_template('src/project/nest.html')

@page.route('/steps/')
def steps():
    return render_template('src/project/steps.html')

@page.route('/otto/')
def otto():
    return render_template('src/project/otto.html')

@page.route('/buddaya/')
def buddaya():
    return render_template('src/project/buddaya.html')

@page.route('/python-articles/')
def articles():
    return render_template('src/update.html')