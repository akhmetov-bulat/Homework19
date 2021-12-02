from dao.model.genre import Genre


class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        genre = self.session.query(Genre).get(gid)
        return genre

    def get_all(self):
        genres = []
        for genre in self.session.query(Genre).all():
            genres.append(genre)
        return genres

    # def create(self, genre_json):
    #     try:
    #         new_genre = Genre(**genre_json)
    #         self.session.add(new_genre)
    #         self.session.commit()
    #         return new_genre.to_json()
    #     except:
    #         return False
    #
    # def update(self, gid, genre_json):
    #     try:
    #         self.session.query(Genre).filter(Genre.id == gid).update(genre_json)
    #         self.session.commit()
    #         return 'True'
    #     except Exception as e:
    #         return e
    #
    #
    # def delete(self, gid):
    #     try:
    #         genre = self.get_one(gid)
    #         self.session.delete(genre)
    #         self.session.commit()
    #         return True
    #     except:
    #         return False