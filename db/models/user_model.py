from uuid import uuid4
from sqlalchemy import UUID, Column, String, Boolean
from db.base import ModelBase

class Users(ModelBase):
    
    __tablename__ = "user_credentials"
    
    id = Column(UUID, primary_key = True, default = uuid4)
    name = Column(String(), nullable = False)
    email = Column(String(), nullable = False)
    password = Column(String(), nullable = False)
    application = Column(String(), nullable = False)
    is_premium = Column(Boolean, nullable = False)
    
    
    def __repr__(self):
        return (
            f"** user_credentials ** "
            f"id : {self.id} "
            f"name : {self.name}"
            f"email : {self.email}"
            f"password : {self.password}"
            f"application : {self.application}"
            f"is_premium : {self.is_premium}"
        )