from setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
    table_keys = {"id", "name"}

    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def to_json(self):
        json_data = {"id": self.id,
                     "name": self.name,
                     }
        return json_data


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
