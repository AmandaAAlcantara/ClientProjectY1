import os
from flask import Flask, redirect, request,render_template, jsonify

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
allpageMessage = "This is the breaking news"
messagesDirectory = {'GoingViral':'The virus R factor is currently 5',
                     'ContactUs':'Today we will be in Cardiff',
                     'Symptoms': ["symptom1", "symptom2","symptom3"]}

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




if __name__ == "__main__":
    app.run(debug=True)
