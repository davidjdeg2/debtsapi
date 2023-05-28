from flask import jsonify, request
from werkzeug.security import check_password_hash
from user import User

def create_auth_blueprint(app):
    auth_bp = Blueprint('auth', __name__)

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data['username']
        password = data['password']
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid username or password'}), 401
        # At this point, the user has been authenticated successfully
        # You might generate and return a JWT token here for subsequent authenticated requests
        return jsonify({'message': 'Login successful'}), 200
