#https://github.com/flet-dev/examples/blob/main/python/apps/trolli/src/sidebar.py
import sqlite3


class DataStore:

    def __init__(self):
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()

            cursor.execute("""CREATE TABLE IF NOT EXISTS notes(
                        header TEXT,
                        body TEXT
            )""")

    @staticmethod
    def get_table_data():
        # возвращает строки таблицы в виде [(header, body), (..., ...)]
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()
            cursor.execute("""SELECT * FROM notes""")
            table = cursor.fetchall()
            return table

    @staticmethod
    def add_note(data: list[str, str]):
        # добавляет заметку в базу данных
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()
            header, body = data[0], data[1]
            cursor.execute("SELECT * FROM notes WHERE header = ?", (header,)) # запрос, чтобы проверить 
            row = cursor.fetchall()
            if not row: cursor.execute("""INSERT INTO notes(header, body)
                                       VALUES(?, ?)""", (header, body))
            else: return False

    @staticmethod
    def remove_note(header: str):
        # удаляет заметку из базы данных
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()
            cursor.execute("""DELETE FROM notes WHERE
                           header = ?""", (header,))

    @staticmethod
    def search_note(text: str):
        # поиск заметки в базе данных
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()
            cursor.execute(f"""SELECT * FROM notes WHERE
                           header LIKE '%{text}%' OR body LIKE '%{text}%'""")
            table = cursor.fetchall()
            return table
