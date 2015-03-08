from flask import Flask, render_template, url_for
from get_temp import read_temp
import sqlite3
app = Flask(__name__)




@app.route('/')
def hello_world():

	temp = read_temp()
	print temp
	return render_template('index.html',temp=temp)

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)