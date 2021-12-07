from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, PWD_HASH_ALGO, SECRET, algo
import hashlib
import random, string
import datetime, calendar, jwt

def hash_password(user_password, salt_db):
    salt = ''.join([PWD_HASH_SALT, salt_db]).encode("utf-8")
    try:
        hash_password = hashlib.pbkdf2_hmac(PWD_HASH_ALGO,
                                            user_password.encode("utf-8"),
                                            salt,
                                            PWD_HASH_ITERATIONS
                                            ).hex()
    except:
        return None
    return hash_password


def generate_salt():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8,16)
    salt_db = ''.join(random.choice(chars) for x in range(size))
    if salt_db:
        return salt_db
    return None

def create_token(data):
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data["exp"] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(data, SECRET, algorithm=algo)
    days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
    data["exp"] = calendar.timegm(days130.timetuple())
    refresh_token = jwt.encode(data, SECRET, algorithm=algo)
    token = {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
    return token, 201


def compare_password(input_password, db_password, db_salt):
    if hash_password(input_password, db_salt) == db_password:
        return True
    return False

