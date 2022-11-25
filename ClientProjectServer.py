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








@app.route("/Whitson", methods = ['GET'])
def returnCheckpointB():
    if request.method =='GET':
        print("staring")
        try:
            # TODO (2) retrieve all public students here
            # connect to the Database,
            # create a cursor object and execute the SQL on that
            # Retrieve the data from the cursor
            # close is in the finally block. un comment it
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
