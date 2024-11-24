from uuid import uuid4
from sqlalchemy import UUID, Column, String
from db.base import ModelBase

class Blogs(ModelBase):
    
    __tablename__ = "blogs"
    
    id = Column(UUID, primary_key = True, default = uuid4)
    title = Column(String(), nullable = False)
    content = Column(String(), nullable = False)
    created_by = Column(String(), nullable = False)
    
    
    def __repr__(self):
        return (
            f"** user_credentials ** "
            f"id : {self.id} "
            f"title : {self.title}"
            f"created_by : {self.created_by}"
        )
