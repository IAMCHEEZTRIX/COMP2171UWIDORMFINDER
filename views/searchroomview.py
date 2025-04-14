from flask import render_template
from core.user import User

class SearchRoomView:
    __user = None
    
    def __init__(self, user: User):
        self.__user = user
    
    def index(self):
        return render_template('searchroom.html', user=self.__user)