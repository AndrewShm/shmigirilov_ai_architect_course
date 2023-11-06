import psycopg2
from psycopg2 import Error

try:
    # подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  password="0000",
                                  host="localhost",
                                  port="5432",
                                  database="demo")

    # курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # выполнить запрос
    cursor.execute("SELECT * FROM bookings.second_task")
    # получить результат
    record = cursor.fetchall()
    print(record)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")