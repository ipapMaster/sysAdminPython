# Работа с БД Python (на примере SQL Lite)
# CRUD - Create Read Update Delete
# Postgre - psycopg2
# MySql - mysql-connector-python
# SQL - PyODBC
import sqlite3

# Подключение
con = sqlite3.connect('address_book.db')

# Создание курсора (для запросов)
cur = con.cursor()

# Запрос
query = """SELECT * FROM persons"""

# Выполняем запрос
result = cur.execute(query).fetchall()

# при Create, Update и Delete
con.commit()

# print(result[0][1])

# Закрываем соединение с БД
con.close()


