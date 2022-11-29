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


@app.route("/TheWetlandsCentre", methods=['GET'])
def CheckpointsD():
    if request.method == 'GET':
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT * FROM Checkpoints WHERE ID = '4';")
            data = cur.fetchall()
        except:
            print("There was an error!")
        finally:
            return render_template('TheWetlandsCentre.html',data=data)


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


@app.route("/Redwick", methods=['GET'])
def CheckpointA():
    if request.method == 'GET':
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT * FROM Checkpoints WHERE ID = '1';")
            data = cur.fetchall()
            print('Hello')
        except:
            print("Error occured")
        finally:
            return render_template("Redwick.html", data=data)
        return render_template('Redwick.html')

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
