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

@app.route("/Location", methods=['GET'])
def returnLocation():
        if request.method == 'GET':
            return render_template('Location.html')

@app.route("/Page4", methods=['GET'])
def returnFourth():
    if request.method == 'GET':
        return render_template('page4.html')


#@app.route("/TheWetlandsCentre", methods=['GET'])
#def CheckpointsD():
    #if request.method == 'GET':
        #try:
            #conn = sqlite3.connect(DATABASE)
            #cur = conn.cursor()
            #cur.execute("SELECT * FROM Checkpoints WHERE ID = '4';")
            #data = cur.fetchall()
        #except:
            #print("There was an error!")
        #finally:
            #return render_template('TheWetlandsCentre.html',data=data)


#@app.route("/GoldcliffSeaWall", methods=['GET'])
#def CheckpointC():
    #if request.method == 'GET':
        #try:
            #conn = sqlite3.connect(DATABASE)
            #cur = conn.cursor()
            #cur.execute("SELECT * FROM Checkpoints WHERE ID = '3';")
            #data = cur.fetchall()
            #print('Hello')
        #except:
            #print("Error occured")
        #finally:
            #return render_template("GoldcliffSeaWall.html", data=data)
        #return render_template('GoldcliffSeaWall.html')


#@app.route("/Redwick", methods=['GET'])
#def CheckpointA():
    #if request.method == 'GET':
        #try:
            #conn = sqlite3.connect(DATABASE)
            #cur = conn.cursor()
            #cur.execute("SELECT * FROM Checkpoints WHERE ID = '1';")
            #data = cur.fetchall()
            #print('Hello')
        #except:
            #print("Error occured")
        #finally:
            #return render_template("Redwick.html", data=data)
        #return render_template('Redwick.html')

#@app.route("/Whitson", methods = ['GET'])
#def returnCheckpointB():
    #if request.method =='GET':
        #print("staring")
        #try:

            #conn = sqlite3.connect(DATABASE)
            #print("connecting to database")
            #cur = conn.cursor()
            #cur.execute("SELECT * FROM Checkpoints WHERE ID = '2';")
            #data = cur.fetchall()
        #except:
            #print('there was an error')
        #finally:
            #conn.close()
            #return render_template('Whitson.html' ,data=data)

@app.route("/Location/<checkpoints>", methods=['GET','POST'])
def retrunCheck(checkpoints= None):
        if request.method =='GET':

            try:
                conn = sqlite3.connect(DATABASE)
                print("connecting to database")
                cur = conn.cursor()
                cur.execute("SELECT * FROM Checkpoints WHERE ID = ?",[checkpoints])
                data = cur.fetchall()
            except:
                print('there was an error')
            finally:
                #conn.close()
                return render_template('info.html',data=data, id=id)



#Enquiry page
@app.route("/Enquiries", methods = ['POST','GET'])
def Enquiry():
    if request.method == 'GET':
        return render_template('Enquiries.html')
    if request.method == 'POST':
        text = request.form.get('text',default="Error")
        email = request.form.get('email',default="Error")
        print("TO DO" + text)

        try:
            conn = sqlite3.connect(DATABASE2)
            cur = conn.cursor()
            cur.execute("INSERT INTO Enquiries ('Text','Email')VALUES (?,?)",
            (text,email))
            conn.commit()
            msg = "Thank you for sending us an enquiry"
        except:
            conn.rollback()
            msg = "failed"
        finally:
            return msg
            conn.close()




if __name__ == "__main__":
    app.run(debug=True)
