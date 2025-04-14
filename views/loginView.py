from flask import render_template, request, session
from models.UsersModel import UsersModel
from views.dashboardView import Dashboard
from models.database import Database
from core.user import User

# MVC
# Model View Control
# Model = database
# View = html files
# Control = route
class Login:

    
    def index(self):
        return render_template('login.html')
    
    
    def login(self):
 
        # session.pop('_flashes', None)
        
        self.userID = int(request.form.get('userID'))
        self.password = request.form.get('password')
    
        
        self.user = UsersModel(self.userID, self.password).getUser()

        if self.user.getuserID() != None:
            
            session['user'] = self.user.to_dict()
                  
            return Dashboard(self.user).index()
            
        
        return self.index()
    
    
        #     if self.user:
            
        #     session['user'] = self.user.to_dict()
            
        #     selectQuery = 'SELECT * from users where usertype = %s'
        #     selectValue = ('Admin',)
            
            
        #     adminUsers = Database().exec(selectQuery, selectValue, fetch=True)
        #     users = []
        #     for user in adminUsers:
        #        users.append(User(user))
            
        #     return Dashboard(self.user).index(values=users)
            
        
        # return self.index()
        