from flask import Flask
from models import db
from auth import auth

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
app.register_blueprint(api_bp, url_prefix='/api')
auth.init_app(app)

if __name__ == '__main__':
        app.run()
