import sqlite3
from datetime import datetime

now = datetime.now()

try:
    dbcon = sqlite3.connect('gimnuroki_data.db')
    con_cursor = dbcon.cursor()



    ##############################
    # Данные уроки по классам
    mass_set = [
        ('Математика', 5),
        ('Русский язык', 5),
        ('Литература', 5),
        ('Математика', 6),
        ('Русский язык', 6),
        ('Литература', 6)
    ]
    text_q = """INSERT INTO urokiklassa
                          (urok, klass)
                          VALUES (?, ?);"""

    for data_set in mass_set:
        con_cursor.execute(text_q, data_set)
        dbcon.commit()

    con_cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (dbcon):
        dbcon.close()
