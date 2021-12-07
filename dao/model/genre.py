from setup_db import db
from marshmallow import Schema, fields


class Genre(db.Model):
    table_keys = {"id", "name"}

    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
