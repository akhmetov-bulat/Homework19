from setup_db import db
from dao.movie import MovieDao
from service.movie import MovieService

from dao.genre import GenreDao
from service.genre import GenreService

from dao.director import DirectorDao
from service.director import DirectorService

from dao.user import UserDao
from service.user import UserService

from service.auth import AuthService

movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDao(db.session)
genre_service = GenreService(genre_dao)

user_dao = UserDao(db.session)
user_service = UserService(user_dao)

auth_service = AuthService(user_dao)