from flask import Flask, render_template, url_for,g,jsonify
from get_temp import read_temp	
import sqlite3
import get_temp as gt
import sensors
app = Flask(__name__)
DATABASE = 'tempdb.db'

sensors = [sensors.Sensor(i) for i in sensors.sensors]

def connect_to_database():
	conn = sqlite3.connect('tempdb.db')
	
	return conn

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def hello_world():

	temps = [i.read() for i in sensors]

	return render_template('index.html',temps=temps)


@app.route('/graph')
def graph():
	c = get_db().cursor()
	query = c.execute('''SELECT * from air;''')
	temps = query.fetchall()
	

	print "graph",temps

	return jsonify(temps=temps)

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)