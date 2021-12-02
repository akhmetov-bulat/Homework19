from setup_db import db
from dao.movie import MovieDao
from service.movie import MovieService

movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)