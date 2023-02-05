import mariadb
# from flask import Flask
import dbcreds
# import json

conn = mariadb.connect(
            user=dbcreds.user,
            password=dbcreds.password,
            host=dbcreds.host,
            port=dbcreds.port,
            database=dbcreds.database,
            autocommit = True
            )

cursor = conn.cursor()
# app = Flask(__name__)

def get_animals():
    cursor.execute("CALL get_animals")
    result = cursor.fetchall()
    print(result)

def add_animals():
    name = input("Animal to add:\n")
    cursor.execute("CALL add_animals(?)",[name])
    cursor.execute("CALL get_animals")
    result = cursor.fetchall()
    print(result)

def remove_animals():
    name = input("Animal to remove:\n")
    cursor.execute("CALL remove_animals(?)",[name])
    cursor.execute("CALL get_animals")
    result = cursor.fetchall()
    print(result)

get_animals()
add_animals()
remove_animals()
# app.run(debug=True)