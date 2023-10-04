import sqlite3


class DataStore:
    # Определение класса для работы с базой данных SQLite.

    def __init__(self):
        # Конструктор. Выполняется при создании нового экземпляра класса.

        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()

            # Создание таблицы "notes" с полями "header" и "body",
            # если она ещё не существует.
            cursor.execute("""CREATE TABLE IF NOT EXISTS notes(
                           header TEXT,
                           body TEXT
                           )""")

    @staticmethod
    def get_table_data():
        # Возвращает все записи из таблицы "notes".

        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()

            # Выполнение SELECT-запроса ко всем записям в таблице.
            cursor.execute("""SELECT * FROM notes""")
            table = cursor.fetchall()
            return table

    @staticmethod
    def add_note(data: list[str, str]):
        # Добавляет новую запись в таблицу "notes".

        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()
            header, body = data[0], data[1]

            # Проверка, существует ли уже запись с таким header.
            cursor.execute("SELECT * FROM notes WHERE header = ?", (header,))
            row = cursor.fetchall()

            # Если такой записи еще нет, осуществляется вставка новой записи.
            if not row:
                cursor.execute("""INSERT INTO notes(header, body)
                                VALUES(?, ?)""", (header, body))
            else:
                return False

    @staticmethod
    def remove_note(header: str):
        # Удаление записи из базы данных по значению header.

        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()

            # Выполнение DELETE-запроса, чтобы удалить запись с заданным header.
            cursor.execute("""DELETE FROM notes WHERE
                           header = ?""", (header,))

    @staticmethod
    def search_note(text: str):
        # Поиск записей, где header или body содержат заданный текст.
        
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()

            # Выполнение SELECT-запроса, чтобы найти записи,
            # содержащие заданный текст в header или body.
            cursor.execute(f"""SELECT * FROM notes WHERE
                           header LIKE '%{text}%' OR body LIKE '%{text}%'""")
            table = cursor.fetchall()
            return table
