from flask import Flask
import json
from dbhelpers import run_statement

app = Flask(__name__)

@app.get('/animals')
def get_animals():
    results = run_statement('CALL get_animals(?)',[])
    if(type(results) == list):
        get_animals_json = json.dumps(results, default=str)
        return get_animals_json
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