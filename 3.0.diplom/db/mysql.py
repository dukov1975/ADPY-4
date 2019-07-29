import mysql.connector
from db.db_config import HOST, DB, USER, PASSWORD


class MySQLdb:

    def __connect(self):
        try:
            conn = mysql.connector.connect(host=HOST, database=DB, user=USER, password=PASSWORD)
        except mysql.connector.Error as error:
            print(error)
        return conn

    def insert_to_db(self, args):

        try:
            conn = self.__connect()
            cursor = conn.cursor()
            cursor.execute(('INSERT INTO users (id, photo, likes) VALUES (%s, %s, %s)'), args)
            conn.commit()
            conn.close()
        except mysql.connector.Error as error:
            print(error)

    def select_from_db(self, args):

        try:
            conn = self.__connect()
            cursor = conn.cursor()
            cursor.execute(('SELECT * FROM users WHERE id=%s'), args)
            result = cursor.fetchall()
            conn.close()
        except mysql.connector.Error as error:
            print(error)
        return result

    def create_table(self):
        try:
            conn = self.__connect()
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE users ('
                           'id INT NOT NULL, '
                           'photo INT NOT NULL DEFAULT 0, '
                           'likes INT NOT NULL DEFAULT 0)')
            conn.commit()
            conn.close()
        except mysql.connector.Error as error:
            print(error)

    def check_table_exists(self):
        try:
            conn = self.__connect()
            cursor = conn.cursor()
            cursor.execute('SELECT count(*) FROM users')
            cursor.fetchall()
            conn.close()
        except mysql.connector.Error as error:
            if error.errno == 1146:
                self.create_table()


