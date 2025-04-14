from flask import render_template, request
from core.user import User
from models.UsersModel import UsersModel
from .dashboardView import Dashboard
from models.database import Database

class AdminAccountPage:
    __user = None
    
    def __init__(self, user: dict):
        self.__user = User(user)
    
    def index(self):
        return render_template('admin_account_page.html',user=self.__user, form_data=[], errors=[])
    
    def creatAdminAccount(self):
        
        value=int(request.form.get('adminID'))
        
        # Validate user input
        self.adminID = self.validate(value=int(request.form.get('adminID')), checkEmpty=True, checkType=True, type=int)
        self.fName = self.validate(request.form.get('first_name'), checkEmpty=True, checkType=True, type=str)
        self.lName = self.validate(request.form.get('last_name'), checkEmpty=True, checkType=True, type=str)
        self.mName = self.validate(request.form.get('middle_name'), checkType=True, type=str)
        self.gender = self.validate(request.form.get('gender'), checkEmpty=True, checkType=True, type=str)
        self.email = self.validate(request.form.get('email'), checkEmpty=True, checkType=True, type=str)
        self.telephone = self.validate(request.form.get('telephone'), checkType=True, type=str)
        
        # Add User to the database
        UsersModel(User({
            'userID': self.adminID,
            'fName': self.fName,
            'lName': self.lName,
            'mName': self.mName,
            'gender': self.gender,
            'email': self.email,
            'telephone': self.telephone ,
            'userType': "Admin",
            'userStatus': 'Active',
            'password': '1234'
        })).addUser()
        
        # Get All Admin accounts
        selectQuery = 'SELECT * from users where usertype = %s'
        selectValue = ('Admin',)
        
        
        adminUsers = Database().exec(selectQuery, selectValue, fetch=True)
        users = []
        for user in adminUsers:
           users.append(User(user))
        
        return Dashboard(self.__user).index(values=users)
        
    
    
    def validate(self, value, checkEmpty=False, checkType=False, type=None):

        # Check for empty values
        if checkEmpty and (value is None or value == ""):
            return False

        # Check for correct type
        if checkType and type is not None:
            if not isinstance(value, type):
                return False

        return value
        
        
        
        
        
        