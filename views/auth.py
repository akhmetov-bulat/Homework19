from flask_restx import Namespace, Resource, abort
from implemented import auth_service
from flask import request

from views.helpers import auth_required

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get('username', None)
        password = req_json.get('password', None)
        if None in [username, password]:
            abort(400)
        token = auth_service.auth_get_token(username, password)
        if not token:
            abort(401, error="Неверные учётные данные")
        return token, 201


    def put(self):
        req_json = request.json
        refresh_token = req_json.get("refresh_token")
        if refresh_token is None:
            abort(400)
        token = auth_service.auth_refresh_token(refresh_token)
        if not token:
            abort(401, error="Неверные учётные данные")
        return token, 201
