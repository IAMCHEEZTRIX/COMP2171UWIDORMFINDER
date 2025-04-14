from flask import Blueprint, session, redirect, url_for, request, render_template
from views.dashboardView import Dashboard
from views.adminAccountView import AdminAccountPage
from views.homeView import Home
from views.searchroomview import SearchRoomView
from core.user import User, Student, Admin
from models.RoomModel import RoomModel
from models.ApplicationModel import ApplicationModel

application_bp = Blueprint('application', __name__)

@application_bp.route('/submit_application/<int:room_id>/<string:action>', methods=['GET','POST'])
def submitApplication(room_id, action):
    errors = {}
    
    if request.method == 'POST':
        
        # Cannot book the same room more than one time
        room_id = int(request.form.get('room_id'))
        room = RoomModel().get_room_by_id(room_id)
        
        user_id = int(request.form.get('student_id'))
        user = Student(user_id)
        
        data = request.form
        
        if user.already_has_application_for_room(room_id):
            errors['room'] = 'You\'ve already booked the selected room'
        
        student_id = request.form.get('student_id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        middle_name = request.form.get('middle_name')
        email = request.form.get('email')
        telephone = request.form.get('telephone')
        gender = request.form.get('gender')
        education_level = request.form.get('education_level')
        program_type = request.form.get('programType')
        reason_for_applying = request.form.get('reason_for_applying')
        co_curricular_activities = request.form.get('co_curricular_activities')
        agreement = True if request.form.get('agreement') else False
        
        # Validation
        if not student_id:
            errors['student_id'] = 'Student ID is required.'
        elif  not int(student_id) == int(User(session['user']).getuserID()):
            errors['student_id'] = 'You cannot book a room using a student ID different from the one you used to log in'
        
        
        if not first_name:
            errors['first_name'] = 'First Name is required.'

        if not last_name:
            errors['last_name'] = 'Last Name is required.'

        if not email:
            errors['email'] = 'Email is required.'
        elif '@' not in email:  # Simple email validation
            errors['email'] = 'Enter a valid email address.'

        if not telephone:
            errors['telephone'] = 'Telephone number is required.'

        if not gender:
            errors['gender'] = 'Gender is required.'

        if not education_level:
            errors['education_level'] = 'Level of Education is required.'

        if not program_type:
            errors['program_type'] = 'Program Type is required.'

        if not reason_for_applying:
            errors['reason_for_applying'] = 'Reason for applying is required.'

        if not agreement:
            errors['agreement'] = 'You must accept the agreement.'

        # If errors exist, return the form with error messages
        if errors:
            return render_template('book_room.html', errors=errors, room=room, form_data=request.form)

        
        form_data = {
            'user_id': request.form['student_id'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'middle_name': request.form.get('middle_name'),
            'email': request.form['email'],
            'telephone': request.form['telephone'],
            'gender': request.form['gender'],
            'education_level': request.form['education_level'],
            'program_type': request.form['programType'],
            'reason_for_applying': request.form['reason_for_applying'],
            'co_curricular_activities': request.form.get('co_curricular_activities'),
            'agreement': True if request.form.get('agreement') else False,
            'room_id': int(room_id),
            'status': "Pending"
        }
        
        user.bookRoom(room, form_data)
        
        return redirect(url_for('dashboard.dashboard'))
    

@application_bp.route('/track_application/<int:room_id>/<int:user_id>', methods=['GET','POST'])
def trackApplication(room_id, user_id):
    statuses = ['pending', 'approved', 'rejected', 'under_review']

    room = RoomModel().get_room_by_id(room_id)
    user = Student(user_id)

    if room_id:
        # Fetch the specific application by room_id and student_id
        application = ApplicationModel().get_application_by_room_and_student(room_id, user_id)
        if application:
            
            applications_with_rooms = [
                {"application": application, "room": room}
            ]
        else:
            applications_with_rooms = []
    else:
        # Fetch all applications for the student
        applications = ApplicationModel().get_all_applications_by_student(user_id)
        applications_with_rooms = [
            {
                "application": application,
                "room": ""
            }
            for application in applications
        ]

    return render_template(
        'track_application.html',
        applications_with_rooms=applications_with_rooms,
        statuses=statuses,
        enumerate=enumerate,
        user = user
    )
    
@application_bp.route('/upload_receipt', methods=['GET','POST'])
def upload_receipt(room_id, user_id):
    pass


@application_bp.route('/approve/<int:application_id>/', methods=['GET','POST'])
def approveApplocation(application_id):
    ApplicationModel().update_application_status(application_id, 'approved')
    
    return Dashboard(Admin(session['user'])).index()

@application_bp.route('/reject/<int:application_id>/', methods=['GET','POST'])
def rejectApplication(application_id):
    ApplicationModel().update_application_status(application_id, 'rejected')
    
    return Dashboard(Admin(session['user'])).index()

