from dao.model.movie import Movie


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        movie = self.session.query(Movie).get(mid)
        if movie:
            return movie.to_json()
        return False

    def get_all(self):
        movies = []
        for movie in self.session.query(Movie).all():
            movies.append(movie)
        if movies:
            return movies
        return False

    def create(self, movie_json):
        try:
            new_movie = Movie(**movie_json)
            self.session.add(new_movie)
            self.session.commit()
            return new_movie.to_json()
        except:
            return False

    def update(self, mid, movie_json):
        try:
            self.session.query(Movie).filter(Movie.id == mid).update(movie_json)
            self.session.commit()
            return 'True'
        except Exception as e:
            return e


    def delete(self, mid):
        try:
            movie = self.get_one(mid)
            self.session.delete(movie)
            self.session.commit()
            return True
        except:
            return False