from flask import Blueprint, session, redirect, url_for, request, render_template
from views.dashboardView import Dashboard
from views.adminAccountView import AdminAccountPage
from views.homeView import Home
from views.searchroomview import SearchRoomView
from core.user import User
from models.RoomModel import RoomModel

bookroom_bp = Blueprint('bookroom', __name__)

@bookroom_bp.route('/bookroom/<int:room_id>/<string:action>', methods=['GET','POST'])
def bookroom(room_id, action):
    
    if action == 'book':
        user = User(session['user'])
        u = user.getuserID()
        
        room = RoomModel().get_room_by_id(room_id)
        
        form_data = {
            'student_id': user.getuserID() if user.getuserID() != None else '',
            'first_name': user.getfName() if user.getuserID() != None else '',
            'last_name': user.getlName() if user.getuserID() != None else '',
            'email': user.getemail() if user.getuserID() != None else '',  
            'action': action,
            'room_id':room.get_room_id()
        }
        
    
    return render_template('application.html', room=room, errors={}, form_data=form_data, user=user)