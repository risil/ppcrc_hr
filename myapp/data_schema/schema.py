from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    age = fields.Int()
    gender = fields.Str()
    mobile = fields.Str()
    email = fields.Str(required=True)
    passport = fields.Str()
    aadhar = fields.Str()
    pancard = fields.Str()
    access_level = fields.Int()

class UserPut(Schema):
    id = fields.Str(required=True)
    first_name = fields.Str()
    last_name = fields.Str()
    age = fields.Int()
    gender = fields.Str()
    mobile = fields.Str()
    email = fields.Str()
    passport = fields.Str()
    aadhar = fields.Str()
    pancard = fields.Str()
    access_level = fields.Int()

class ManagerSchema(Schema):
    id = fields.String()
    user = fields.String()
    designation = fields.String()
    created_at = fields.DateTime()
    created_by = fields.String()
    updated_at = fields.DateTime()
    updated_by = fields.String()
    is_deleted = fields.Integer()

class ManagerPutSchema(Schema):
    id = fields.String(required=True)
    user = fields.String()
    designation = fields.String()
