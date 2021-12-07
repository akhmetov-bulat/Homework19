
class MovieService:
    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def get_first(self):
        return self.movie_dao.first()

    def get_one(self, mid):
        return self.movie_dao.get_one(mid)

    def get_all(self,director_id, genre_id, year):
        return self.movie_dao.get_all(director_id=director_id, genre_id=genre_id, year=year)

    def create(self, movie_json):
        movie = self.movie_dao.create(movie_json)
        return movie

    def update(self, mid, movie_json):
        return self.movie_dao.update(mid = mid, movie_json=movie_json)


    def delete(self, mid):
        return self.movie_dao.delete(mid=mid)
