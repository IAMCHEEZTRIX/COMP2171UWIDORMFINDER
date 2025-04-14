from flask import Blueprint, session, redirect, url_for, request
from views.dashboardView import Dashboard
from views.adminAccountView import AdminAccountPage
from views.homeView import Home
from views.searchroomview import SearchRoomView
from core.user import User

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
def dashboard():
    
    return Dashboard(User(session['user'])).index()



@dashboard_bp.route('/room_search', methods=['GET'])
def room_search():
    return SearchRoomView(User(session['user'])).index()


@dashboard_bp.route('/admin_account_page/<int:userID>', methods=['GET'])
def admin_account_page(userID):
    user = session['user']
    # Ensuring that its the same user that was verified and login (calling this page)
    if session['user']['userID'] == userID:
        
        return AdminAccountPage(session['user']).index()
    
    return Home().index()

@dashboard_bp.route("/logout", methods=["POST", "GET"])
def logout():
    session.clear()
    return redirect(url_for('login.login'))