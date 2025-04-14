from models.database import Database
from .room import Room
from .application import Application
from models.ApplicationModel import ApplicationModel

class User:
    _userID = None
    _fName = None
    _lName = None
    _mNane = None
    _gender = None
    _telephone = None
    _email = None
    _userType = None
    _userStatus = None
    _password = None
    _db = Database()
    
    # def __init__(self, user_data: list):
    #     self.__userID = user_data[0][0]
    #     self.__fName = user_data[0][1]
    #     self.__lName = user_data[0][2]
    #     self.__email = user_data[0][3]
    #     self.__userType = user_data[0][4]
    #     self.__userStatus = user_data[0][5]
    #     self.__password = user_data[0][6]
        
    def __init__(self, user_data: dict):
        
        if isinstance(user_data, int):
            self.__initialize_from_db(user_data)
        else:
            if len(user_data) != 0:
            
                if isinstance(user_data, list):
                    self._userID = user_data[0][0]
                    self._fName = user_data[0][1]
                    self._lName = user_data[0][2]
                    self._mNane = user_data[0][3]
                    self._gender = user_data[0][4]
                    self._email = user_data[0][5]
                    self._telephone = user_data[0][6]
                    self._userType = user_data[0][7]
                    self._userStatus = user_data[0][8]
                    self._password = user_data[0][9]
                elif isinstance(user_data, tuple):
                    self._userID = user_data[0]
                    self._fName = user_data[1]
                    self._lName = user_data[2]
                    self._mNane = user_data[3]
                    self._gender = user_data[4]
                    self._email = user_data[5]
                    self._telephone = user_data[6]
                    self._userType = user_data[7]
                    self._userStatus = user_data[8]
                    self._password = user_data[9]
                else:
                    self._userID = user_data['userID']
                    self._fName = user_data['fName']
                    self._lName = user_data['lName']
                    self._mNane = user_data['mName']
                    self._gender = user_data['gender']
                    self._email = user_data['email']
                    self._telephone = user_data['telephone']
                    self._userType = user_data['userType']
                    self._userStatus = user_data['userStatus']
                    self._password = user_data['password']
    
    
    def __initialize_from_db(self, user_id: int):
        """Fetch user data from database and initialize attributes"""
        query = "SELECT * FROM users WHERE user_id = %s"
        result = self._db.exec(query, (user_id,), fetch=True)
        
        if not result:
            raise ValueError(f"User with ID {user_id} not found")
        
        # Assuming result is a list of tuples (adjust if your DB returns differently)
        user_data = result[0]
        
        self._userID = user_data[0]
        self._fName = user_data[1]
        self._lName = user_data[2]
        self._mName = user_data[3]
        self._gender = user_data[4]
        self._email = user_data[5]
        self._telephone = user_data[6]
        self._userType = user_data[7]
        self._userStatus = user_data[8]
        self._password = user_data[9]
            
    def to_dict(self):
        return {
            'userID': self._userID,
            'fName': self._fName,
            'lName': self._lName,
            'mName': self._mNane,
            'gender': self._gender,
            'email': self._email,
            'telephone': self._telephone ,
            'userType': self._userType,
            'userStatus': self._userStatus,
            'password': self._password,
        }
        
    
    def getuserID(self):
        return self._userID
    
    def getfName(self):
        return self._fName
    
    def getlName(self):
        return self._lName
    
    def getmName(self):
        return self._mNane
    
    def getgender(self):
        return self._gender
    
    def getemail(self):
        return self._email
    
    def gettelephone(self):
        return self._telephone
    
    def getuserType(self):
        return self._userType
    
    def getuserStatus(self):
        return self._userStatus
    
    def getpassword(self):
        return self._password
    
    def getAllApplications(self):
        applications = ApplicationModel().get_All_applications_by_user(self)
        return applications
    
    
class Student(User):
    
    def __init__(self, user_data):
        super().__init__(user_data)
        
    
    def bookRoom(self, room: Room, form_data):
        application = Application(form_data)
        ApplicationModel().create_application(self, room, application)
        

    def editApplication():
        pass
    
    def uploadPaymentReceipt():
        pass
    
    def already_has_application_for_room(self, room_id) -> bool:
        query = "SELECT 1 FROM applications WHERE user_id = %s and room_id= %s LIMIT 1"
        result = self._db.exec(query, (self.getuserID(), room_id,), fetch=True)
        return bool(result)
    

class Admin(User):
    
    def __init__(self, user_data):
        super().__init__(user_data)
    
    def approveApplication():
        pass
    
    def rejectApplication():
        pass
    
    def editApplication():
        pass  
    
    def getAllApplications(self):
        applications = ApplicationModel().get_all_applications()
        return applications
    
class IT(User):
    
    def __init__(self, user_data):
        super().__init__(user_data)
    
    def createAdminAccount():
        pass
    
    #   Update the name for the users classes 
    