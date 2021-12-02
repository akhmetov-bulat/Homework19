from dao.model.movie import Movie, MovieSchema
from flask_restx import Resource, Namespace
from implemented import movie_service
from flask import request, jsonify, Response

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        movies = movie_service.get_all()
        if movies:
            return movies, 200
        return 'not found', 404

    def post(self):
        movie = movie_service.create(request.json)
        if not movie:
            return "create error", 400
        # Правильно ли отправил заголовок?
        return {"Content-Location": f"/movies/{movie['id']}"}, 201


@movie_ns.route('/<int:mid>')
class MovieViewMid(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        if movie:
            return movie, 200
        return "not found", 404

    def put(self, mid):
        movie_json = request.json
        if set(movie_json.keys()) == Movie.table_keys:
            if movie_json["id"] == mid:
                if movie_service.update(mid, movie_json):
                    return "updated", 200
            return "wrong data", 400
        return "keys not equals", 400

    def patch(self, mid):
        movie_json = request.json
        response = movie_service.update(mid, movie_json)
        if response == 'True':
            return "", 200
        return str(response), 400

    def delete(self, mid):
        if movie_service.delete(mid):
            return "", 204
        return "wrong data", 400
