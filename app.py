from flask import Flask
from config import Config
from setup_db import db
from flask_restx import Api
from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.users import user_ns
from views.auth import auth_ns
from dao.database.utils import init_db



def create_app(cfg):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(cfg)
    db.init_app(app)
    return app


def register_extensions(app):
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    init_db(app, db)


cfg = Config()
app = create_app(cfg)
register_extensions(app)

if __name__ == '__main__':
    app.run()