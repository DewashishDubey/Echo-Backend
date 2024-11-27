from marshmallow import Schema, fields, post_load
from db.models.user_model import Users
import uuid

class UserSchema(Schema):
    id = fields.UUID(required = False)
    name = fields.String(required = True)
    email = fields.String(required = True)
    password = fields.String(required = True)
    application = fields.String(required = False)
    is_preimum = fields.Boolean(required = False)

    @post_load
    def make_user(self, data, **kwargs):
        return Users(**data)
