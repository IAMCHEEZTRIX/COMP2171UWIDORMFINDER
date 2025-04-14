from flask import Blueprint, request
from views.loginView import Login


login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    loginObj = Login()
    
    if request.method == "POST":
        return loginObj.login()
    
    return loginObj.index()