import datetime
from db.base import db
from db.models.user_model import Users
import jwt
from settings import Settings

class Auth:
    def __init__(self) -> None:
        pass
    
    def login(self, email, password):
        existing_user = Users.query.filter_by(email = email, password = password, application = 'echo').first()

        if existing_user:
            payload = {
                'username': existing_user.name,
                'email' : email,
                'application': 'echo',  
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  
            }
            token = jwt.encode(payload, Settings.SECRET_KEY, algorithm='HS256')

            return {'resp_code': 2000, 'resp_msg': 'Login successful', 'token': token}
        
        return {'resp_code': 1001, 'resp_msg': 'Incorrect Password or account does not exist'}
    
    def register(self, username, email, password):
        existing_user = Users.query.filter_by(email = email).first()

        if existing_user:
            return {'resp_code': 1001, 'resp_msg': 'User already exists, login to continue'}
        
        user = Users(name = username, email = email, password = password, application = 'echo', is_premium = False)
        db.session.add(user)
        db.session.commit()
        return {'resp_code': 2000, 'resp_msg': 'Account Created Successfully'}
        