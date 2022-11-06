import sqlite3
from datetime import datetime
import os
from config import path_movies

###########################
# Проверка пользователя
def check_users(user_id):
    res = []
    try:
        dbcon = sqlite3.connect('gimnuroki_data.db')
        con_cursor = dbcon.cursor()

        text_q = "select klass, name from users where idtelegramm=?"
        data_set = (user_id,)
        con_cursor.execute(text_q,data_set)
        records = con_cursor.fetchall()
        for row in records:
            res.append([row[0],row[1]])
        con_cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (dbcon):
            dbcon.close()
    return res

########################################
## проверка пароля
def check_psw_klass(psw):
    res = []
    try:
        dbcon = sqlite3.connect('gimnuroki_data.db')
        con_cursor = dbcon.cursor()

        text_q = "select password, klass from psw_klass where password=?"
        data_set = (psw,)
        con_cursor.execute(text_q,data_set)
        records = con_cursor.fetchall()
        for row in records:
            res.append([row[0], row[1]])

        con_cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (dbcon):
            dbcon.close()
    return res

#########################
# Регистрация пользователя
def registr_uses(user_id,klass,name,username):
    res = []
    try:
        dbcon = sqlite3.connect('gimnuroki_data.db')
        con_cursor = dbcon.cursor()
        now = datetime.now()

        text_q = "select klass, name from users where idtelegramm=?"
        data_set = (user_id,)
        con_cursor.execute(text_q,data_set)
        records = con_cursor.fetchall()
        if len(records) == 0:
            data_set = (user_id, name, username, klass, now)
            print(">>>:", data_set)
            text_q = """INSERT INTO users
                                  (idtelegramm, name, username, klass, joining_date)
                                  VALUES (?, ?, ?, ?, ?);"""
        else:
            data_set = (klass, user_id)
            text_q = "Update users set klass = ? where idtelegramm = ?"

        con_cursor.execute(text_q, data_set)
        dbcon.commit()

        con_cursor.close()
        res.append([klass, user_id])

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (dbcon):
            dbcon.close()
    return res

########################################
## Выдает список предметов класса
def get_urokiklassa(klass):
    res = []
    try:
        dbcon = sqlite3.connect('gimnuroki_data.db')
        con_cursor = dbcon.cursor()

        text_q = "select urok from urokiklassa where klass=?"
        data_set = (klass,)
        con_cursor.execute(text_q,data_set)
        records = con_cursor.fetchall()
        for row in records:
            res.append(row[0])

        con_cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (dbcon):
            dbcon.close()
    return res

########################################
## Выдает список предметов класса
def get_moviesuroka(urok, klass):
    files = os.listdir(path_movies+str(klass)+"/"+str(urok))
    return files

#print(get_urokiklassa(5))
#registr_uses(123321, 5, "tx_user", "tx_username")

#print(check_psw_klass("1234"))
print(get_moviesuroka("math", 5))