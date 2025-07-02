from flask import render_template, Blueprint
from models.model import social_media

routes = Blueprint('main', __name__)

@routes.route('/')
def index():
    return render_template('index.html', social_media=social_media)