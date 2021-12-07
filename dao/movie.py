from dao.model.movie import Movie, MovieSchema
from sqlalchemy import text

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        movie = self.session.query(Movie).get(mid)
        return movie

    def get_all(self, director_id, genre_id, year):
        params = {}
        if director_id:
            params['director_id'] = director_id
        if genre_id:
            params['genre_id'] = genre_id
        if year:
            params['year'] = year
        if params:
            movies = self.session.query(Movie).filter_by(**params).all()
        else:
            movies = self.session.query(Movie).all()
        return movies

    def create(self, movie_json):
        try:
            new_movie = Movie(**movie_json)
            self.session.add(new_movie)
            self.session.commit()
            return new_movie
        except:
            pass

    def update(self, mid, movie_json):
        try:
            self.session.query(Movie).filter(Movie.id == mid).update(movie_json)
            self.session.commit()
            return True
        except:
            return False


    def delete(self, mid):
        try:
            movie = self.get_one(mid)
            self.session.delete(movie)
            self.session.commit()
            return True
        except:
            return False
