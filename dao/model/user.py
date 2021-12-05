from setup_db import db
from marshmallow import Schema, fields


class User(db.Model):
    table_keys = {"id", "username", "password", "salt", "role"}
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    salt = db.Column(db.String)
    role = db.Column(db.String)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    password = fields.Str(load_only=True)
    salt = fields.Str(load_only=True)
    role = fields.Str()
