

def check_database():
    from constants import DB_FILENAME
    from os.path import isfile
    if not isfile(DB_FILENAME):
        return False
    return True


def init_db(app, db):
    from dao.model import movie, genre, director, user
    from service.utils import generate_salt, hash_password
    import csv

    with app.app_context():
        db.drop_all()
        db.create_all()
        with db.session.begin():
            entities = []
            with open('./dao/database/movies.csv', 'r', encoding='UTF-8') as f:
                for item in csv.DictReader(f):
                    item['rating'] = item['rating'].replace(',', '.')
                    entities.append(movie.Movie(**item))
            with open('./dao/database/genres.csv', 'r', encoding='UTF-8') as f:
                for item in csv.DictReader(f):
                    entities.append(genre.Genre(**item))
            with open('./dao/database/directors.csv', 'r', encoding='UTF-8') as f:
                for item in csv.DictReader(f):
                    entities.append(director.Director(**item))
            u1 = user.User(username="vasya", password="my_little_pony", role="user")
            u1.salt = generate_salt()
            u1.password = hash_password(u1.password, u1.salt)
            u2 = user.User(username="oleg", password="qwerty", role="user")
            u2.salt = generate_salt()
            u2.password = hash_password(u2.password, u2.salt)
            u3 = user.User(username="oleg2", password="P@ssw0rd", role="admin")
            u3.salt = generate_salt()
            u3.password = hash_password(u3.password, u3.salt)
            db.session.add_all([u1, u2, u3])
            db.session.add_all(entities)
