import psycopg2
import json
from flask import Flask

db_name = 'user1'
db_host = 'db'
db_user = 'user1'
db_password = 'password'

app = Flask(__name__)
conn = psycopg2.connect(database=db_name, user=db_user,
    password=db_password, host=db_host)

@app.route('/hw10')
def index():
        cur = conn.cursor()
        cur.execute("SELECT * FROM HW10_TABLE")
        res = cur.fetchall()
        cur.close()
#        return str(res)
        return json.dumps(res)

#app.route('/data')(index)

if __name__ == '__main__':
    app.run()
