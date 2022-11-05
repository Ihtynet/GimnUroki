import sqlite3
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

        text_q = "select password, klass from psw_klass where password=? and klass=?"
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

print(check_psw_klass("1234"))
print(check_users("1234567891"))