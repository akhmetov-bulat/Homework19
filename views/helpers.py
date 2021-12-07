import jwt
from flask import abort, request
from constants import SECRET, algo


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, SECRET, algorithms=[algo])
        except:
            abort(401)
        return func(*args, **kwargs)
    return wrapper


def self_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        try:
            decoded_data = jwt.decode(token, SECRET, algorithms=[algo])
        except:
            abort(401)
        if decoded_data["id"] != kwargs['uid']:
            abort(403)
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        try:
            user = jwt.decode(token, SECRET, algorithms=[algo])
            role = user.get("role")
            if role != "admin":
                abort(401)
        except:
            abort(401)
        return func(*args, **kwargs)
    return wrapper