from flask import Blueprint, request, session
from views.adminAccountView import AdminAccountPage
from views.homeView import Home

create_admin_account_bp = Blueprint('createAdmin', __name__)

@create_admin_account_bp.route('/create_admin_account', methods=['GET', 'POST'])
def create_admin_account():
    
    if request.method == "POST":
        return AdminAccountPage(session['user']).creatAdminAccount()
    
    return Home().index()