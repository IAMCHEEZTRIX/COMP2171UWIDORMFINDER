from flask import render_template

class Home:
    
    def index(self):
        return render_template('index.html')
    
