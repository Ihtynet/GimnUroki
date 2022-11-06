import sqlite3
from datetime import datetime

###########################
# Проверка пользователя
def check_users(user_id):
    res = []
    try:
        dbcon = sqlite3.connect('gimnuroki_data.db')
        con_cursor = dbcon.cursor()

        text_q = "select klass, student from users where idtelegramm=?"
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
def registr_uses(user_id,klass,name,student):
    res = []
    try:
        dbcon = sqlite3.connect('gimnuroki_data.db')
        con_cursor = dbcon.cursor()
        now = datetime.now()
        text_q = """INSERT INTO users
                              (idtelegramm, name, student, klass, joining_date)
                              VALUES (?, ?, ?, ?, ?);"""
        data_set = (user_id, name, student, klass, now)
        con_cursor.execute(text_q, data_set)
        dbcon.commit()

        con_cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (dbcon):
            dbcon.close()
    return res

#registr_uses(123321, 5, "tx_user", "tx_username")

#print(check_psw_klass("1234"))
#print(check_users("1234567891"))