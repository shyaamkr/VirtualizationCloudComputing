from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
   conn = sqlite3.connect('exercise.db')
   conn.row_factory = sqlite3.Row
   return conn

@app.route('/data'. methods=['GET'])
def get_data():
   conn = get_db_connection()
   rows = conn.execute('select * from exercise').fetchall()
   conn.close()
   return jsonify([dict[row] for row in rows])

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000)
