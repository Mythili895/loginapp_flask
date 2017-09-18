from __future__ import print_function 
from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import abort
from flask import jsonify
import os
import sys
import datetime
from flask_mysqldb import MySQL
import time
#import MYSQLdb

from flask_cors import CORS, cross_origin
from flask import Flask, render_template, redirect, \
    url_for, request, session, flash, g
from functools import wraps

import errno
global new_session
new_session = ''



app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql3.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql3194599'
app.config['MYSQL_PASSWORD'] = 'l4YptXN8tG'
app.config['MYSQL_DB'] = 'sql3194599'
app.config['MYSQL_USE_UNICODE'] = False

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mysql = MySQL(app)



 
@app.route("/" , methods=['POST','GET'])
def index():
        new_session = ''
        #print('Hello world!', file=sys.stderr)
        return render_template('firstpage.html')
        

@app.route("/newexist", methods=['POST'])
def newexist():
        global new_session
        new_session = ''
	if request.method == 'POST':
		if request.form['submit'] == 'newuser':
			return render_template('signup.html')

		elif request.form['submit'] == 'existinguser':
			return render_template('signin.html')	

@app.route("/login", methods=['POST'])
def login():                   
        
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    rv = get_exist(POST_USERNAME, POST_PASSWORD)
    #print (str(rv), file=sys.stderr)
   # details = rv.split(',')
    #print (rv, file=sys.stderr)
    if rv == "Enter username":
        return render_template('login_extra.html', message = "Enter Username")
    if rv == "Enter Password":
        return render_template('login_extra.html', message = "Enter Password")    
    if rv == "12":
        cur=mysql.connection.cursor()
        global new_session
        new_session = POST_USERNAME
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        cur.execute('''INSERT INTO date_time (username,time) VALUES (%s,%s)''' , (POST_USERNAME,timestamp))
        mysql.connection.commit()
        sample = []
        cur.execute("""SELECT time
                  FROM date_time 
                  WHERE username=%s 
                  """,
               [POST_USERNAME])
        t = cur.fetchall()
        for i in t:
                (tim,) = i
                sample.append(tim)
        
        
        return render_template('user.html',name=POST_USERNAME, t=sample)
    elif rv== "1":
        return render_template('wrong_user.html')

@app.route('/logging', methods=['GET', 'POST'])
@cross_origin()
def logging():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == 'GET':
        global new_session    
        #print(new_session,file=sys.stderr)
        filename = new_session + " " +"user" +".log"
        filename1 = new_session + " " +"user"+ "_mouse_traj" + ".log"
        f = open(filename, "a+")
        f1 = open(filename1, "a+")
        #with ((as f ) and () as f1)):
        te = str(request.args.get('Message'))
        mess = str(timestamp) +  "   " +  te + "\n"
        if(te != "None" and "mouse movement trajectory:" not in te):
                f.write(mess)
		if "You closed the page" in te:
			f.close()
			f1.close()
			return render_template('firstpage.html')
        if("mouse movement trajectory:"  in te):
                f1.write(mess)
						
                    
        
        #print(te,file=sys.stderr)
        return request.args.get('Message')        


@app.route("/succ_signup", methods=['POST'])
def succ_signup():                   
        
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    cur=mysql.connection.cursor()
    cur.execute('''INSERT INTO user_account (username,password) VALUES (%s,%s)''' , (POST_USERNAME,POST_PASSWORD))
    mysql.connection.commit()
    return render_template('succ_signup.html',name=POST_USERNAME, password=POST_PASSWORD)


def get_exist(username , passw):
    a = "1"
    
    if username == "":
        return "Enter username"

    if passw == "":
        return "Enter Password"    
    cur=mysql.connection.cursor()
    cur.execute("""SELECT username
                  FROM user_account 
                  WHERE username=%s 
                  """,
               [username])
    t = cur.fetchall()
    if str(t) == "()":
        a = "1"
        return a

    ((u,),) = t
    


    cur.execute("""SELECT password
                  FROM user_account 
                  WHERE username=%s 
                  """,
               [username])
    ((pw,),) = cur.fetchall()
    #print (rv, file=sys.stderr)

    if pw == passw:
        a = "12"
    return a



 
if __name__ == "__main__":
    
    app.run()
