from marshmallow import Schema, fields, post_load
from db.models.blog_model import Blogs
import uuid

class BlogSchema(Schema):
    id = fields.UUID(required = False)
    title = fields.String(required = True)
    content = fields.String(required = True)
    created_by = fields.String(required = True)

    @post_load
    def make_user(self, data, **kwargs):
        return Blogs(**data)
