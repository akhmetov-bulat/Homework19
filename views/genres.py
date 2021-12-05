from dao.model.genre import Genre, GenreSchema
from flask_restx import Resource, Namespace
from implemented import genre_service
from flask import request

from views.helpers import auth_required, admin_required

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenreView(Resource):
    @auth_required
    def get(self):
        genres = genre_service.get_all()
        if genres:
            return genres_schema.dump(genres), 200
        return 'not found', 404

    @admin_required
    def post(self):
        genre = genre_service.create(request.json)
        if not genre:
            return "create error", 400
        return genre, 201, {'Location': f"/movies/{genre['id']}"}


@genre_ns.route('/<int:gid>')
class GenreViewGid(Resource):

    @auth_required
    def get(self, gid):
        genre = genre_service.get_one(gid)
        if genre:
            return genre_schema.dump(genre), 200
        return "not found", 404

    @admin_required
    def put(self, gid):
        genre_json = request.json
        if set(genre_json.keys()) == Genre.table_keys:
            if genre_json["id"] == gid:
                if genre_service.update(gid, genre_json):
                    return "updated", 200
            return "wrong data", 400
        return "keys not equals", 400

    @admin_required
    def patch(self, gid):
        genre_json = request.json
        if genre_service.update(gid, genre_json):
            return "", 200
        return "", 400

    @admin_required
    def delete(self, gid):
        if genre_service.delete(gid):
            return "", 204
        return "wrong data", 400
