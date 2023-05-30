from flask import Flask
from models import db
from auth import create_auth_blueprint

create_app(app)

auth_bp = create_auth_blueprint(app)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run()
