from flask import Flask
from .HomeControl import home_bp
from .LoginControl import login_bp
from .DashboardControl import dashboard_bp
from .AdminAccountControl import create_admin_account_bp
from .SearchRoomControl import searchroom_bp
from .BookRoomControl import bookroom_bp
from .ApplicationControl import application_bp

def register_controllers(app: Flask):
    app.register_blueprint(home_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(create_admin_account_bp)
    app.register_blueprint(searchroom_bp)
    app.register_blueprint(bookroom_bp)
    app.register_blueprint(application_bp)
    