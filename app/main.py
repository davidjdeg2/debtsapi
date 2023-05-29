from flask import Flask
from models import db
from auth import create_auth_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.init_app(app)

auth_bp = create_auth_blueprint(app)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run()
