from flask import Flask
import json
# from dbhelpers import run_statement

# try this as there is a problem with my dbhelpers
import mariadb
import dbcreds
conn = mariadb.connect(
                user=dbcreds.user,
                password=dbcreds.password,
                host=dbcreds.host,
                port=dbcreds.port,
                database=dbcreds.database
)

cursor = conn.cursor()
# to here

app = Flask(__name__)

@app.get('/animals')
def get_animals():
    cursor.execute('CALL get_animals')
    results = cursor.fetchall()
    if(type(results) == list):
        get_animals_json = json.dumps(results, default=str)
        return get_animals_json
    else:
        return 'There was an error'

@app.post('/animals')
def add_animals(request):
    input = request.get_json(name)
    name = input['name']
    cursor.execute('CALL add_animals(?)',[name])
    results = cursor.fetchall()
    if(type(results) == list):
        add_animals_json = json.dumps(results, default=str)
        return add_animals_json
    else:
        return 'There was an error'

# def add_animals():
#     name = input("Animal to add:\n")
#     cursor.execute("CALL add_animals(?)",[name])
#     cursor.execute("CALL get_animals")
#     result = cursor.fetchall()
#     print(result)

# def remove_animals():
#     name = input("Animal to remove:\n")
#     cursor.execute("CALL remove_animals(?)",[name])
#     cursor.execute("CALL get_animals")
#     result = cursor.fetchall()
#     print(result)

get_animals()
# add_animals()
# remove_animals()
app.run(debug=True)