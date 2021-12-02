from dao.model.director import Director


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        director = self.session.query(Director).get(did)
        return director

    def get_all(self):
        directors = []
        for director in self.session.query(Director).all():
            directors.append(director)
        return directors

    # def create(self, director_json):
    #     try:
    #         new_director = Director(**director_json)
    #         self.session.add(new_director)
    #         self.session.commit()
    #         return new_director.to_json()
    #     except:
    #         return False
    #
    # def update(self, did, director_json):
    #     try:
    #         self.session.query(Director).filter(Director.id == did).update(director_json)
    #         self.session.commit()
    #         return 'True'
    #     except Exception as e:
    #         return e
    #
    #
    # def delete(self, did):
    #     try:
    #         director = self.get_one(did)
    #         self.session.delete(director)
    #         self.session.commit()
    #         return True
    #     except:
    #         return False