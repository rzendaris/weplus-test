
import sqlite3 as sql
from config import Config


class Database:

    def __init__(self):
        pass

    @staticmethod
    def create_db():
        conn = sql.connect(Config.DATABASE_NAME)
        print ("Create New Database")
        conn.execute(
            'CREATE TABLE IF NOT EXISTS read_my_mind (id INTEGER NOT NULL PRIMARY KEY, number INTEGER, answer VARCHAR)')
        conn.execute(
            'CREATE TABLE IF NOT EXISTS numbers (id INTEGER NOT NULL PRIMARY KEY, number INTEGER)')
        print ("Database Created!")
        conn.close()

    def get_db_connection(self):
        conn = sql.connect(Config.DATABASE_NAME)
        conn.row_factory = sql.Row
        return conn

    def fetch_read_my_mind(self):
        conn = self.get_db_connection()
        read_my_mind = conn.execute('SELECT * FROM read_my_mind').fetchall()
        conn.close()

        return read_my_mind

    def create_read_my_mind(self, number, answer):
        conn = self.get_db_connection()
        conn.execute('INSERT INTO read_my_mind (number, answer) VALUES (?, ?)',
                     (number, answer))
        conn.commit()
        conn.close()

        return True

    def delete_read_my_mind(self):
        conn = self.get_db_connection()
        conn.execute('DELETE FROM read_my_mind')
        conn.commit()
        conn.close()

        return True

    def fetch_numbers(self):
        conn = self.get_db_connection()
        numbers = conn.execute('SELECT * FROM numbers').fetchall()
        conn.close()

        return numbers

    def create_numbers(self):
        numbers = list(range(0, int(Config.MAX_NUMBER) + 1))
        conn = self.get_db_connection()
        for number in numbers:
            conn.execute('INSERT INTO numbers (number) VALUES (?)', (number,))
        conn.commit()
        conn.close()

        return True

    def delete_number_all(self):
        conn = self.get_db_connection()
        conn.execute('DELETE FROM numbers')
        conn.commit()
        conn.close()

        return True

    def delete_number(self, number, equal = False, greater_than=False, all=False):
        if greater_than:
            sql = 'DELETE FROM numbers where number > ?'
        else:
            sql = 'DELETE FROM numbers where number < ?'

        if equal:
            sql = 'DELETE FROM numbers where number = ?'

        conn = self.get_db_connection()
        conn.execute(sql, (number,))
        conn.commit()
        conn.close()

        return True