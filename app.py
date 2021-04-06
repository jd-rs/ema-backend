from flask import Flask, request
import os
import psycopg2

app = Flask(__name__)

DB_PASSWORD = os.environ['DB_PASSWORD']
API_KEY = os.environ['API_KEY']

conn = psycopg2.connect(database="d868cvi8e3ub4m", user = "zhcyugerfzeisx", password = DB_PASSWORD, host = "ec2-54-242-120-138.compute-1.amazonaws.com", port = "5432")
cur = conn.cursor()

sensor_locations = {"001": "Campo Agrario Tec"}

@app.route('/sensors', methods=['POST'])
def sensors():
    if request.form['api_key'] == API_KEY:
        location = sensor_locations[request.form['sensor_id']]
        temperature = request.form['temperature']
        do = request.form['do']
        ph = request.form['ph']

        cur.execute("INSERT INTO sensors(location, temperature, oxygen, ph) VALUES(%s, %s, %s, %s)", (location, temperature, do, ph))
        conn.commit()

        return({'location': location, 'temperature': temperature, 'ph': ph, 'do': do})    
    
