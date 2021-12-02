from flask import Flask
from config import Config
from constants import DB_FILENAME
from setup_db import db
from flask_restx import Api
from views.movies import movie_ns
from dao.model.movie import Movie
from views.utils import init_db, check_database


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    cfg = Config()
    app.config.from_object(cfg)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    init_db(app, db)


app = create_app()

if __name__ == '__main__':
    app.run()