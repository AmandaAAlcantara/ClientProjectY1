import os
from flask import Flask, redirect, request,render_template, jsonify
import sqlite3

DATABASE = 'Checkpoints.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


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

@app.route("/Page3", methods=['GET','POST'])
def returnThird():
        if request.method == 'GET':
            return render_template('page3.html')




@app.route("/Page4", methods=['GET'])
def returnFourth():
    if request.method == 'GET':
        return render_template('page4.html')

@app.route("/Redwick", methods=['GET'])
def CheckpointA():
    if request.method == 'GET':
        print("starting")
        try:
            conn = sqlite3.connect(DATABASE)
            print("connectobg")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Checkpoints WHERE ID = '1';")
            data = cur.fetchall()
        except:
            print("error")
        finally:
            return render_template('Redwick.html', data=data)


@app.route("/Whitson", methods = ['GET'])
def returnCheckpointB():
    if request.method =='GET':
        print("staring")
        try:

            conn = sqlite3.connect(DATABASE)
            print("connecting to database")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Checkpoints WHERE ID = '2';")
            data = cur.fetchall()
        except:
            print('there was an error')
        finally:
            #conn.close()
            return render_template('Whitson.html' ,data=data)


if __name__ == "__main__":
    app.run(debug=True)
