import os
from flask import Flask, redirect, request,render_template, jsonify
import sqlite3

DATABASE = 'Checkpoints.db'
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','gif'])

app = Flask(__name__)

@app.route("/Home", methods=['GET'])
def returnHome():
    if request.method == 'GET':
        return render_template('Home.html')

@app.route("/Page1", methods=['GET'])
def returnFirst():
    if request.method == 'GET':
        return render_template('page1.html')

@app.route("/Page2", methods=['GET'])
def returnSecond():
    if request.method == 'GET':
        return render_template('page2.html')

@app.route("/Page3", methods=['GET'])
def returnThird():
    if request.method == 'GET':
        return render_template('page3.html')

@app.route("/Page4", methods=['GET'])
def returnFourth():
    if request.method == 'GET':
        return render_template('page4.html')

@app.route("/GoldcliffSeaWall", methods=['GET'])
def CheckpointC():
    if request.method == 'GET':
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT * FROM Checkpoints WHERE ID = '3';")
            data = cur.fetchall()
            print('Hello')
        except:
            print("Error occured")
        finally:
            return render_template("GoldcliffSeaWall.html", data=data)
        return render_template('GoldcliffSeaWall.html')



if __name__ == "__main__":
    app.run(debug=True)
