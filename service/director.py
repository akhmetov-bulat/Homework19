

class DirectorService:
    def __init__(self, director_dao):
        self.director_dao = director_dao

    def get_first(self):
        return self.director_dao.first()

    def get_one(self, did):
        return self.director_dao.get_one(did)

    def get_all(self):
        return self.director_dao.get_all()

    def create(self, director_json):
        director = self.director_dao.create(director_json)
        return director

    def update(self, did, director_json):
        return self.director_dao.update(did = did, director_json=director_json)


    def delete(self, did):
        return self.director_dao.delete(did=did)
