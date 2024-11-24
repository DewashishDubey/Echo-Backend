from flask import request, Blueprint
from api.modules.auth.auth import Auth

auth_views = Blueprint('auth_views', __name__)
auth_obj = Auth()

@auth_views.route('/api/v1/login', methods=['POST'])
def login():
    global auth_obj
    email = request.args.get('email')
    password = request.args.get('password')
    return auth_obj.login(email = email, password = password)

@auth_views.route('/api/v1/register', methods=['POST'])
def register():
    global auth_obj
    username = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')
    return auth_obj.register(username = username, email = email, password = password)
    
    
    