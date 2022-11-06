import sqlite3
from datetime import datetime

now = datetime.now()


try:
    dbcon = sqlite3.connect('gimnuroki_data.db')
    con_cursor = dbcon.cursor()

    text_q = "select sqlite_version();"
    con_cursor.execute(text_q)
    record = con_cursor.fetchall()
    print("Версия базы данных SQLite: ", record)


    ########################
    # Таблица пользователей канала
    text_q = """CREATE TABLE users ( 
             id INTEGER PRIMARY KEY,
             idtelegramm TEXT NOT NULL,  
             name TEXT,  
             username text,  
             joining_date timestamp,  
             klass INTEGER NOT NULL 
             );"""
    con_cursor.execute(text_q)
    dbcon.commit()

    ########################
    # Таблица уроки по классам
    text_q = """CREATE TABLE urokiklassa ( 
             id INTEGER PRIMARY KEY,
             urok TEXT NOT NULL,  
             klass INTEGER NOT NULL 
             );"""
    con_cursor.execute(text_q)
    dbcon.commit()

    ########################
    # Таблица паролей по классам
    text_q = """CREATE TABLE psw_klass ( 
             id INTEGER PRIMARY KEY,  
             password TEXT NOT NULL,  
             klass INTEGER NOT NULL 
             );"""
    con_cursor.execute(text_q)
    dbcon.commit()

    ##############################
    # Данные паролей
    text_q = """INSERT INTO psw_klass
                          (password, klass)
                          VALUES ('1234', '5');"""
    con_cursor.execute(text_q)
    dbcon.commit()

    ##############################
    # Данные пользователей
    data_set = (12345678910, 'Alex', 'Иванов Иван', 1, now)
    text_q = """INSERT INTO users
                          (idtelegramm, name, username, klass, joining_date)
                          VALUES (?, ?, ?, ?, ?);"""
    con_cursor.execute(text_q,data_set)
    dbcon.commit()

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
        con_cursor.execute(text_q,data_set)
        dbcon.commit()

    con_cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (dbcon):
        dbcon.close()
