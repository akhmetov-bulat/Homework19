from dao.model.user import User


class UserDao:
    def __init__(self, session):
        self.session = session

    def check_username(self, username):
        if self.session.query(User).filter(User.username == username).first():
            return True
        return False

    def get_by_username(self, username):
        user = self.session.query(User).filter(User.username == username).first()
        if user:
            return user
        return None

    def get_one(self, uid):
        user = self.session.query(User).get(uid)
        if user:
            return user
        return None

    def get_all(self):
        users = []
        for user in self.session.query(User).all():
            users.append(user)
        if users:
            return users
        return None

    def create(self, user_json):
        try:
            new_user = User(**user_json)
            self.session.add(new_user)
            self.session.commit()
            return new_user
        except:
            return None

    def update(self, user_json):
        try:
            self.session.query(User).filter(User.id == user_json.get["id"]).update(user_json)
            self.session.commit()
            return True
        except:
            return False


    def delete(self, uid):
        try:
            user = self.get_one(uid)
            self.session.delete(user)
            self.session.commit()
            return True
        except:
            return False
