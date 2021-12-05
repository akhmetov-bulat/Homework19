from dao.model.user import User, UserSchema
from flask_restx import Resource, Namespace
from implemented import user_service
from flask import request

from views.helpers import admin_required

user_schema = UserSchema()
users_schema = UserSchema(many=True)

user_ns = Namespace('users')


@user_ns.route('/')
class UserView(Resource):
    def get(self):
        users = user_service.get_all()
        if users:
            return users_schema.dump(users), 200
        return 'not found', 404

    def post(self):
        username = request.json.get("username")
        if user_service.check_username(username):
            return "user already exists", 400
        user = user_service.create(request.json)
        if not user:
            return "create error", 400
        user_json = user_schema.dump(user)
        return user_json, 201, {'Location': f"/users/{user_json['id']}"}


@user_ns.route('/<int:uid>')
class UserViewGid(Resource):
    def get(self, uid):
        users = user_service.get_one(uid)
        if users:
            return user_schema.dump(users), 200
        return "not found", 404


    def put(self, uid):
        user_json = request.json
        if "salt" not in user_json.keys():
            user_json["salt"] = ""
        if set(user_json.keys()) == User.table_keys:
            if user_json["id"] == uid:
                if user_json["password"] != "":
                    if user_service.update(user_json):
                        return "updated", 200

            return "wrong data", 400
        return "keys not equals", 400


    def patch(self, uid):
        users_json = request.json
        try:
            if uid == users_json.get("id")\
                    and user_service.update(users_json):
                return "", 200
        except:
            return "wrong data", 400

    @admin_required
    def delete(self, uid):
        if user_service.delete(uid):
            return "", 204
        return "wrong data", 400


