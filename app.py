import mariadb
from flask import Flask
import dbcreds
import json

conn = mariadb.connect(
            user=dbcreds.user,
            password=dbcreds.password,
            host=dbcreds.host,
            port=dbcreds.port,
            database=dbcreds.database,
            autocommit = True
            )

app = Flask(__name__)



app.run(debug=True)