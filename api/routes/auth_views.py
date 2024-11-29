from flask import request, Blueprint
from api.modules.auth.auth import Auth

auth_views = Blueprint('auth_views', __name__)
auth_obj = Auth()

@auth_views.route('/api/v1/login', methods=['POST'])
def login():
    global auth_obj
    user_data = request.get_json()
    return auth_obj.login(user_data = user_data)

@auth_views.route('/api/v1/register', methods=['POST'])
def register():
    global auth_obj
    user_data = request.get_json()
    return auth_obj.register(user_data = user_data)
    
    
    