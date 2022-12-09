import os
from flask import Flask, redirect, request,render_template, jsonify
import sqlite3

DATABASE = 'ClientProject.db'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)


@app.route("/Home", methods=['GET'])
def returnHome():
    if request.method == 'GET':
        return render_template('Home.html')

@app.route("/ChooseyourRoutes", methods=['GET'])
def Routes():
    if request.method == 'GET':
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT * FROM Routes;")
            naturewalksdata = cur.fetchall()
            cur.execute("SELECT * FROM RoutesC;")
            citywalksdata = cur.fetchall()
            data = cur.fetchall()
        except:
            print("There was an error!")
        finally:
            return render_template('ChooseyourRoutes.html',naturewalksdata = naturewalksdata, citywalksdata=citywalksdata)

@app.route("/Difficulty", methods=['GET'])
def returnSecond():
    if request.method == 'GET':
        return render_template('Difficulty.html')

@app.route("/Location", methods=['GET'])
def returnLocation():
        if request.method == 'GET':
            return render_template('Location.html')


@app.route("/Login", methods=['GET'])
def returnLogin():
    if request.method == 'GET':
        return render_template('Login.html')

@app.route("/Events", methods=['GET','POST'])
def retrunEvents():
        if request.method =='GET':

            try:
                conn = sqlite3.connect(DATABASE)
                print("connecting to database")
                cur = conn.cursor()
                cur.execute("SELECT * FROM Events")
                data = cur.fetchall()
            except:
                print('there was an error')
            finally:
                #conn.close()
                return render_template('Events.html',data=data)


@app.route("/Festive5k", methods=['GET'])
def returnFestive5k():
    if request.method == 'GET':
        return render_template('Festive5k.html')

#@app.route("/Admin", methods=['GET'])
#def returnFourth():
#    if request.method == 'GET':
#        return render_template('Admin.html')

@app.route("/Admin", methods = ['POST','GET'])
def AddCheckpoints():
	if request.method =='GET':
		return render_template('Admin.html')
	if request.method =='POST':
		name = request.form.get('name', default="Error")
		picture = request.form.get('picture', default="Error")
		facts = request.form.get('facts', default="Error")
		contacts = request.form.get('contacts', default="Error")
		print("Your checkpoint is "+name)

		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("INSERT INTO Checkpoints ('Name', 'Picture','Facts' , 'Contacts')VALUES (?,?,?,?)",
			(name,picture,facts,contacts,))
			conn.commit()
			msg = "Checkpoint Added"
		except:
			conn.rollback()
			msg = "failed"
		finally:
			return msg
			conn.close()



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

@app.route("/AllCheckpoints", methods = ['GET'])
def SeeCheckpoints():
	if request.method =='GET':
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("SELECT * FROM Checkpoints;")
			data = cur.fetchall()


			print("getting data")
		except:
			print('there was an error',)
		finally:
			conn.close()
			return render_template('AllCheckpoints.html', data =data)

#Enquiry page
@app.route("/Enquiries", methods = ['POST','GET'])
def Enquiry():
    if request.method == 'GET':
        return render_template('Enquiries.html')
    if request.method == 'POST':
        text = request.form.get('text',default="Error")
        email = request.form.get('email',default="Error")
        print("Enquiry:" + text)

        try:
            conn = sqlite3.connect(DATABASE)
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




#Enquiry page

if __name__ == "__main__":
    app.run(debug=True)
