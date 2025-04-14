from models.database import Database
from core.user import User, Student, Admin, IT

class UsersModel:
    __user = None
    __userID = None
    __fName = None
    __lName = None
    __email = None
    __userType = None
    __userStatus = None
    __password = None
    __db = Database()
    
    def __init__(self, *args):
        
        if len(args) == 1 and isinstance(args[0], User):
            self.__user = args[0]
            
        elif len(args) == 1 and isinstance(args[0], int):
            self.__userID = args[0]
        
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], str):
            self.__userID = args[0]
            self.__password = args[1]
        else:
            self.__userID = None
            self.__fName = None
            self.__lName = None
            self.__email = None
            self.__userType = None
            self.__userStatus = None
            self.__password = None
        
        
    
    def addUser(self):
         
        selectQuery = 'SELECT user_id, email from users where user_id = %s or email = %s'
        selectValue = (self.__user.getuserID(), self.__user.getemail())
        
        self.user = self.__db.exec(selectQuery, selectValue, fetch=True)
        
        for user in self.user:

            if user[0] == self.__user.getuserID():
                return f"This user({self.__userID}) is already exist!!"
            
            
            if user[1] == self.__user.getemail():
                return "This email address exist!"
        
         
        query = 'INSERT INTO users (user_id, fname, lname, mname, gender, email, telephone, usertype, userstatus, password) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = (self.__user.getuserID(), self.__user.getfName(), self.__user.getlName(), self.__user.getmName(), self.__user.getgender(), 
                  self.__user.getemail(), self.__user.gettelephone(), self.__user.getuserType(), self.__user.getuserStatus(), self.__user.getpassword())
        
        self.conn = self.__db.exec(query, values)
        
        
    def getUser(self):
        
        query = 'SELECT * FROM users where user_id = %s and password=%s'
        values = (self.__userID,self.__password)
        
        user_data = self.__db.exec(query, values, fetch=True)
        
        if user_data[0][7] == "Student":
            return Student(user_data)
        if user_data[0][7] == "Admin":
            return Admin(user_data)
        if user_data[0][7] == "IT":
            return IT(user_data)
        
        return User(user_data)
        
        
        
        
        
        
        
        