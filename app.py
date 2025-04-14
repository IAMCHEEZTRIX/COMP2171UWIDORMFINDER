from flask import Flask
from controllers import register_controllers


app = Flask(__name__)


# Secret key for session encryption
app.secret_key = 'UWIDORMFINDER'

# Register all Blueprints
register_controllers(app)
    

if __name__ in "__main__":
    app.run(debug=True)