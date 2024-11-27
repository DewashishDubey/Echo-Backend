import datetime
from db.base import db
from db.models.user_model import Users
import jwt
from settings import Settings
from schema.user_schema import UserSchema
from api.utils.validation import validate_and_extract_data
from flask import Flask, request, jsonify

class Auth:
    def __init__(self) -> None:
        self.schema_for_login = UserSchema(only=['email','password'])
        self.schema_for_registeration = UserSchema(only=['name','email','password'])
        pass
    
    def login(self, user_data):
        data,error = validate_and_extract_data(schema = self.schema_for_login, data = user_data)
        if not data or error:
            return{'resp_code' : 998,'resp_msg' : error}

        existing_user = Users.query.filter_by(email = data.email, password = data.password, application = 'echo').first()

        if existing_user:
            payload = {
                'username': existing_user.name,
                'email' : data.email,
                'application': 'echo',  
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  
            }
            token = jwt.encode(payload, Settings.SECRET_KEY, algorithm='HS256')

            return {'resp_code': 2000, 'resp_msg': 'Login successful', 'token': token}
        
        return {'resp_code': 1001, 'resp_msg': 'Incorrect Password or account does not exist'}
    
    def register(self, user_data):
        data,error = validate_and_extract_data(schema = self.schema_for_registeration, data = user_data)
        if not data or error:
            return{'resp_code' : 998,'resp_msg' : error}

        existing_user = Users.query.filter_by(email = data.email).first()

        if existing_user:
            return {'resp_code': 1001, 'resp_msg': 'User already exists, login to continue'}
        
        user = Users(name = data.name, email = data.email, password = data.password, application = 'echo', is_premium = False)
        db.session.add(user)
        db.session.commit()

        return {'resp_code': 2000, 'resp_msg': 'Account Created Successfully'}
        