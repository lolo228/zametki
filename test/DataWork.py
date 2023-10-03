#https://github.com/flet-dev/examples/blob/main/python/apps/trolli/src/sidebar.py
import sqlite3


class DataStore:
    def __init__(self):
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS notes(
                        header TEXT,
                        body TEXT
            )''')

    @staticmethod
    def get_table_data():
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()
            cursor.execute('''SELECT * FROM notes''')
            table = cursor.fetchall()
            return table

    @staticmethod
    def add_note(data: list[str, str]):
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()
            header, body = data[0], data[1]
            cursor.execute("SELECT * FROM notes WHERE header = ?", (header,)) # запрос, чтобы проверить 
            row = cursor.fetchall()
            if not row: cursor.execute('''INSERT INTO notes(header, body) VALUES(?, ?)''', (header, body))
            else: return False

    @staticmethod
    def remove_note(header: str):
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()
            cursor.execute('''DELETE FROM notes WHERE header = ?''', (header,)) #Забываешь скобки, у тебя он вопросики не будет принимать без скобок, если у тебя 1 элемент заятую в конце ебашь, иначе будет падать
    
    @staticmethod
    def search_note(text: str):
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()
            cursor.execute('''SELECT * FROM notes WHERE header = ? OR body = ?''', (text, text))
            table = cursor.fetchall()
            return table
