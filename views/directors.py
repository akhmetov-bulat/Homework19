from dao.model.director import Director, DirectorSchema
from flask_restx import Resource, Namespace
from implemented import director_service
from flask import request, jsonify, Response

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        directors = director_service.get_all()
        if directors:
            return directors_schema.dump(directors), 200
        return 'not found', 404

    # def post(self):
    #     director = director_service.create(request.json)
    #     if not director:
    #         return "create error", 400
    #     return director, 201, {'Location': f"/movies/{director['id']}"}


@director_ns.route('/<int:did>')
class DirectorViewDid(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        if director:
            return director_schema.dump(director), 200
        return "not found", 404

    # def put(self, did):
    #     director_json = request.json
    #     if set(director_json.keys()) == Director.table_keys:
    #         if director_json["id"] == did:
    #             if director_service.update(did, director_json):
    #                 return "updated", 200
    #         return "wrong data", 400
    #     return "keys not equals", 400
    #
    # def patch(self, did):
    #     director_json = request.json
    #     response = director_service.update(did, director_json)
    #     if response == 'True':
    #         return "", 200
    #     return str(response), 400
    #
    # def delete(self, did):
    #     if director_service.delete(did):
    #         return "", 204
    #     return "wrong data", 400
