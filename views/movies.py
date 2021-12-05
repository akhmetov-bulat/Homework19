
from dao.model.movie import Movie, MovieSchema
from flask_restx import Api, Resource, Namespace
from implemented import movie_service
from flask import request, jsonify, Response

from flask_restx import reqparse

from views.helpers import auth_required, admin_required

parser = reqparse.RequestParser()
parser.add_argument("director_id", type=int, location='args')
parser.add_argument("genre_id", type=int, location='args')
parser.add_argument("year", type=int, location='args')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieView(Resource):

    # @auth_required
    @movie_ns.expect(parser)
    def get(self):
        director_id = parser.parse_args()["director_id"]
        genre_id = parser.parse_args()["genre_id"]
        year = parser.parse_args()["year"]
        # director_id = request.args.get('director_id')
        # genre_id = request.args.get('genre_id')
        # year = request.args.get('year')
        movies = movie_service.get_all(drctr=director_id, gnr=genre_id, yr=year)
        if movies:
            return movies_schema.dump(movies), 200
        return "", 404

    @admin_required
    def post(self):
        movie = movie_service.create(request.json)
        if not movie:
            return "create error", 400
        return movie_schema.dump(movie), 201, {'Location': f"/movies/{movie['id']}"}


@movie_ns.route('/<int:mid>')
class MovieViewMid(Resource):

    @auth_required
    def get(self, mid):
        movie = movie_service.get_one(mid)
        if movie:
            return movie_schema.dump(movie), 200
        return "not found", 404

    @admin_required
    def put(self, mid):
        movie_json = request.json
        if set(movie_json.keys()) == Movie.table_keys:
            if movie_json["id"] == mid:
                if movie_service.update(mid, movie_json):
                    return "updated", 200
            return "wrong data", 400
        return "keys not equals", 400

    @admin_required
    def patch(self, mid):
        if movie_service.update(mid, request.json):
            return "", 200
        return "", 400

    @admin_required
    def delete(self, mid):
        if movie_service.delete(mid):
            return "", 204
        return "not found", 404
