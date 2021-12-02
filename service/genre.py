from dao.model.genre import Genre


class GenreService:
    def __init__(self, genre_dao):
        self.genre_dao = genre_dao

    def get_first(self):
        return self.genre_dao.first()

    def get_one(self, gid):
        return self.genre_dao.get_one(gid)

    def get_all(self):
        return self.genre_dao.get_all()

    def create(self, genre_json):
        genre = self.genre_dao.create(genre_json)
        return genre

    def update(self, gid, genre_json):
        return self.genre_dao.update(gid = gid, genre_json=genre_json)


    def delete(self, gid):
        return self.genre_dao.delete(gid=gid)
