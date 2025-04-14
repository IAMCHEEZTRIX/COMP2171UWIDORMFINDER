from flask import render_template
from core.user import User
from models.database import Database

class Dashboard:
    __user = None
    
    def __init__(self, user: User):
        self.__user = user
    
    def index(self):
        dashboardData = []
        if self.__user.getuserType() == "Student":
            dashboardData = self.__user.getAllApplications()
            
        if self.__user.getuserType() == "Admin":
            dashboardData = self.__user.getAllApplications()
            
        if self.__user.getuserType() == "IT":
            selectQuery = 'SELECT * from users where usertype = %s'
            selectValue = ('Admin',)
            
            
            adminUsers = Database().exec(selectQuery, selectValue, fetch=True)
            
            for user in adminUsers:
                dashboardData.append(User(user))
        
        return render_template('dashboard.html', user=self.__user, values=dashboardData)