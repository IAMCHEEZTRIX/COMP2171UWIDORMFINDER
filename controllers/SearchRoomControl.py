from flask import Blueprint, session, redirect, url_for, request, render_template
from views.dashboardView import Dashboard
from views.adminAccountView import AdminAccountPage
from views.homeView import Home
from views.searchroomview import SearchRoomView
from core.user import User
from models.RoomModel import RoomModel

searchroom_bp = Blueprint('searchroom', __name__)

@searchroom_bp.route('/search_room', methods=['POST'])
def search_room():
    u = session['user']
    user = User(session['user'])
    
    if user.getuserType() not in ['Student', 'Admin']:
        return redirect(url_for('dashboard.dashboard'))
    
    rooms = []
    if request.method == 'POST':
        room_type = request.form.get('room_type')
        dormitory = request.form.get('dormitory')  
        level = request.form.get('level')  
        availability = request.form.get('availability')
        
        # Query the database based on the search criteria
        # Create filters dictionary
        filters = {
            'room_type': room_type,
            'building': dormitory,
            'floor_number': level,
            'available_rooms': availability  # Or other availability logic
        }
        
        # Get filtered rooms
        rooms = RoomModel().getRooms(filters)
        
    
    return render_template('searchroom.html', rooms=rooms, user=User(session['user']))