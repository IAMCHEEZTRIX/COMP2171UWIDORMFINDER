from flask import Blueprint
from views.homeView import Home

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    return Home().index()