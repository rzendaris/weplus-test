
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
            'CREATE TABLE IF NOT EXISTS read_my_mind (id INTEGER NOT NULL PRIMARY KEY, number INTEGER, answer VARCHAR)');
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