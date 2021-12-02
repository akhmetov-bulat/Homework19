from constants import DB_FILENAME


class Config():
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILENAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    HOST = "localhost"
    PORT = 5000
    JSON_AS_ASCII = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    JSON_SORT_KEYS = False
    SECRET_HERE = 'asdkljfh87y3245kjlbasjkhdgvb'