import sqlite3

class SQLighter():
    """docstring for SQLighter"""
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    
    def create(self):
        querry = '''CREATE TABLE users(
                        id Int,
                        cur_dev Int
                    );'''
        self.cursor.execute(querry)
        
        querry = """CREATE TABLE devices(
                        id int,
                        user_id int, 
                        cap text,
                        ip text
                    );"""
        self.cursor.execute(querry)

    def get_current_device(self, user_id):
        querry = "SELECT cur_dev FROM users WHERE id = {0}".format(user_id)
        self.cursor.execute(querry)
        return cursor.fetchone()

    def add_user(self, user_id):
        querry = "INSERT INTO users VALUES({0}, -1)".format(user_id)
        self.cursor.execute(querry)
        self.connection.commit()

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()