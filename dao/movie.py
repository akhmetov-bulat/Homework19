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

    def get_all(self, drctr, gnr, yr):
        parameters_list = []
        if drctr:
            parameters_list.append(f"director_id == {int(drctr)}")
        if gnr:
            parameters_list.append(f"genre_id == {int(gnr)}")
        if yr:
            parameters_list.append(f"year == {int(yr)}")
        parameters = " AND ".join(parameters_list)
        movies = self.session.query(Movie).filter(text(f"{parameters}")).all()
        # if drctr:
        #     if gnr:
        #         if yr:
        #             movies = self.session.query(Movie).filter(Movie.director_id == int(drctr),
        #                                                       Movie.genre_id == int(gnr),
        #                                                       Movie.year == int(yr)).all()
        #         else:
        #             movies = self.session.query(Movie).filter(Movie.director_id == int(drctr),
        #                                                       Movie.genre_id == int(gnr)).all()
        #     elif yr:
        #         movies = self.session.query(Movie).filter(Movie.director_id == int(drctr),
        #                                                   Movie.year == int(yr)).all()
        #     else:
        #         movies = self.session.query(Movie).filter(Movie.director_id == int(drctr)).all()
        # elif yr:
        #     movies = self.session.query(Movie).filter(Movie.year == int(yr)).all()
        # elif gnr:
        #     movies = self.session.query(Movie).filter(Movie.genre_id == int(gnr)).all()
        # else:
        #     movies = self.session.query(Movie).all()
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
