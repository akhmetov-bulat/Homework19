from constants import DB_FILENAME


def check_database():
    from os.path import isfile, getsize
    if not isfile(DB_FILENAME):
        return False
    # elif getsize(DB_FILENAME) < 40000:
    #     return False
    '''здесь я хотел проверить базу на пустоту, не получилось.
    getsize(db_filename) выдает постоянно 32768 при созданных трех таблицах без данных
    и с заполненными данными в таблице movies
    '''
    return True


def init_db(app, db):
    from dao.model import movie, genre, director
    import csv

    with app.app_context():
        db.drop_all()
        db.create_all()
        with db.session.begin():
            entities = []
            with open('dao/database/movies.csv', 'r', encoding='UTF-8') as f:
                for item in csv.DictReader(f):
                    entities.append(movie.Movie(**item))
                    print(item)
            with open('dao/database/genres.csv', 'r', encoding='UTF-8') as f:
                for item in csv.DictReader(f):
                    entities.append(genre.Genre(**item))
                    print(item)
            with open('dao/database/directors.csv', 'r', encoding='UTF-8') as f:
                for item in csv.DictReader(f):
                    entities.append(director.Director(**item))
                    print(item)
            db.session.add_all(entities)

