from setup_db import db
from marshmallow import Schema, fields


class Movie(db.Model):
    table_keys = {"id", "title", "description", "trailer", "year", "rating", "genre_id","director_id"}

    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(400))
    trailer = db.Column(db.String(100))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))
    genre = db.relationship('Genre')
    director = db.relationship('Director')




class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
