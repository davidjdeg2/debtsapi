from flask import Flask
from models import db
from auth import auth
from routes import api_bp

app = Flask(__name__)
app.config.from_object('config')

# Register the API blueprint
app.register_blueprint(api_bp)

db.init_app(app)
app.register_blueprint(api_bp, url_prefix='/api')
auth.init_app(app)

if __name__ == '__main__':
        app.run()
