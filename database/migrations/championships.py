import sqlite3
import definitions


def migrate():

    connection = sqlite3.connect(definitions.DB_PATH)

    try:

        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS championships(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            name TEXT NOT NULL,
            created_at timestamp,
            updated_at timestamp,
            deleted_at timestamp)''')

        connection.commit()

    except Exception as e:
        connection.rollback()
        raise e
    finally:
        print("Championships migration completed")
        connection.close()
