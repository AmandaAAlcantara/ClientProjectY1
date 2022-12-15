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

@app.route("/LevelCoastalPath", methods=['GET','POST'])
def returnLevel():
    if request.method == 'GET':
        try:
            conn = sqlite3.connect(DATABASE)
            print("connecting to database")
            cur = conn.cursor()
            cur.execute("SELECT * FROM LevelCoastalPath")
            data = cur.fetchall()
        except:
            print('there was an error')
        finally:
            return render_template('LevelCoastalPath.html',data=data)

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
            cur.execute("SELECT * FROM DisabilityF;")
            disabilitydata = cur.fetchall()
            data = cur.fetchall()
        except:
            print("There was an error!")
        finally:
            return render_template('ChooseyourRoutes.html',naturewalksdata = naturewalksdata, citywalksdata=citywalksdata,disabilitydata=disabilitydata)

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

#@app.route("/Admin", methods=['GET'])
#def returnFourth():
#    if request.method == 'GET':
#        return render_template('Admin.html')
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


@app.route("/AddCheckpoints", methods = ['POST','GET'])
def AddCheckpoints():
	if request.method =='GET':
		return render_template('addCheckpoints.html')
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



@app.route("/AddEvents", methods = ['POST','GET'])
def AddEvent():
	if request.method =='GET':
		return render_template('addEvents.html')
	if request.method =='POST':
		eventdate = request.form.get('eventdate', default="Error")
		eventname = request.form.get('eventname', default="Error")
		eventinfo= request.form.get('eventinfo', default="Error")
		eventtime = request.form.get('eventtime', default="Error")
		print("Your Event is "+eventname)

		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("INSERT INTO Events ('Date', 'Name','Info' , 'Time')VALUES (?,?,?,?)",
			(eventdate,eventname,eventinfo,eventtime,))
			conn.commit()
			msgevent = "Event Added"
		except:
			conn.rollback()
			msgevent = "failed"
		finally:
			return msgevent
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
def enquiry():
	if request.method =='GET':
		return render_template('Enquiries.html')
	if request.method =='POST':
		email = request.form.get('email', default="Error")
		text = request.form.get('text', default="Error")
		print("Your enquiry is "+email)

		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("INSERT INTO Enquiries ('Text', 'Email')VALUES (?,?)",
			(text,email))
			conn.commit()
			msg = "Thank you for sending us an enquiry."
		except:
			conn.rollback()
			msg = "failed"
		finally:
			return msg
			conn.close()









#Comments.html
@app.route("/Commentssubmission" , methods = ['POST','GET'])
def Comments():
      if request.method == 'GET':
             return render_template('Comments.html')
      if request.method == 'POST':
         NameOfRoute = request.form.get('NameOfRoute', default="Error")
         NameOfLocation = request.form.get('NameOfLocation', default="Error")
         Comment = request.form.get('Comment', default="Error")
         print (NameOfRoute)
         print (NameOfLocation)
         print (Comment)


         try:
             conn = sqlite3.connect(DATABASE)
             cur = conn.cursor()
             print ("created cursor")
             # cur.execute("INSERT INTO Commentssubmission ('NameOfRoute','NameOfLocation','Comment')VALUES (?,?,?)" , (NameOfRoute , NameOfLocation , Comments))
             cur.execute("INSERT INTO Commentssubmission ('NameOfRoute','NameOfLocation','Comment')VALUES (?,?,?)" , (NameOfRoute , NameOfLocation , Comment))
             #data = cur.fetchall()
             conn.commit()
             print ("inserted data")
             msg = "Thank you for your comment, we will look into it as soon as possible"
         except Exception as e:
             print(e)
             conn.rollback()
             msg = "Failed"
         finally:
             return msg
             conn.close()
             return render_template('Comments.html', data =data)

@app.route("/AddRoutes", methods = ['POST','GET'])
def AddRoute():
	if request.method =='GET':
		return render_template('addRoutes.html')
	if request.method =='POST':
		routepic = request.form.get('routepic', default="Error")
		routename = request.form.get('routename', default="Error")
		routeinfo= request.form.get('routeinfo', default="Error")
		print("Your Route is "+routename)

		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("INSERT INTO Routes ('Picture', 'Name','Info')VALUES (?,?,?)",
			(routepic,routename,routeinfo,))
			conn.commit()
			msgroute = "Route Added"
		except:
			conn.rollback()
			msgroute = "failed"
		finally:
			return msgroute
			conn.close()


#admin page
@app.route("/Admin", methods=['GET'])
def returnAdmin():
    if request.method == 'GET':
        return render_template('Admin.html')


#admin page
@app.route("/Festive5k", methods=['GET'])
def returnFestive5k():
    if request.method == 'GET':
        return render_template('/Festive5k.html')



if __name__ == "__main__":
    app.run(debug=True)



 #addRoute
