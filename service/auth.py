from service.utils import hash_password, create_token, compare_password


class AuthService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def auth_get_token(self, username, password):
        user = self.user_dao.get_by_username(username)
        if user is None:
            return None
        if compare_password(password, user.password, user.salt):
            data = {
                    "username": user.username,
                    "role": user.role
                    }
            tokens = create_token(data)
            return tokens

    def auth_refresh_token(self, refresh_token):
        import jwt
        from constants import SECRET, algo

        try:
            token_data = jwt.decode(jwt=refresh_token, key=SECRET, algorithms=[algo])
        except:
            return None
        username = token_data.get('username')
        user = self.user_dao.get_by_username(username)
        if user is None:
            return None
        data = {
                "username": user.username,
                "role": user.role
                }
        tokens = create_token(data)
        return tokens
