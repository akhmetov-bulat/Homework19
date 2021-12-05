from service.utils import generate_salt, hash_password


class UserService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def get_salt(self):
        pass

    def get_by_username(self, uid):
        return self.user_dao.get_one(uid)

    # def get_first(self):
    #     return self.user_dao.first()

    def get_one(self, uid):
        return self.user_dao.get_one(uid)

    def get_all(self):
        return self.user_dao.get_all()

    def create(self, user_json):
        data = {"username": user_json.get("username"),
                "password": user_json.get("password"),
                "role": user_json.get("role", "user"),
                }
        if None in data:
            return None
        salt_db = generate_salt()
        hashed_password = hash_password(data["password"], salt_db)
        if None in [hashed_password, salt_db]:
            return None
        data["password"] = hashed_password
        data["salt"] = salt_db
        user = self.user_dao.create(data)
        print(user)
        return user

    def update(self, user_json):

        if user_json["salt"] == "":
            user_json["salt"] = generate_salt()
        user_json["password"] = hash_password(user_json["password"], user_json["salt"])
        return self.user_dao.update(user_json=user_json)


    def delete(self, uid):
        return self.user_dao.delete(uid=uid)



    def check_username(self, username):
        return self.user_dao.check_username(username)


