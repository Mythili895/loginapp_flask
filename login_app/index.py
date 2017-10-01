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
import csv
import datetime
from flask_mysqldb import MySQL
import time
import plotly.plotly as py
import plotly.graph_objs as go
import logging
import numpy as np
import pandas as pd
import logging
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


@app.route("/visualization", methods=['POST','GET'])
def visualization():
        return render_template('visualization.html')


@app.route("/user_options", methods=['POST','GET'])
def user_options():
        
        
        return render_template('user_options.html')

@app.route("/scatterplot_user", methods=['POST','GET'])
def scatterplot_user():
    #csv = np.genfromtxt('aaamouse.csv',delimiter = ",")
    global new_session
    filename = new_session + "mouse.csv"
    f = open(filename , 'a+')
    x_axis = []
    y_axis = []
    link = []
    date =[]
    time =[]
    
    
    reader = csv.reader(f,delimiter = ',')
    for row in reader:
        date .append(row[0])
        time.append(row[1])
        x_axis.append(row[2])
        y_axis.append(row[3])
        link.append(row[4])

    unique_link = set(link)
    unique_link = list(unique_link)
    link_coord_x = []
    link_coord_y = []
    for i in range(len(unique_link)):
            link_coord_x.append([])
            link_coord_y.append([])
    filename1 = new_session + "mouse.csv"
    f1 = open(filename1 , 'a+')        
    reader1 = csv.reader(f1,delimiter = ',')        
    for row in reader1:
            for i in range(len(unique_link)):
                    if str(row[4]) == str(unique_link[i]):
                            link_coord_x[i].append(row[2])
                            link_coord_y[i].append(row[3])
    trace = []
            
    for i in range(len(unique_link)):
           
            trace.append (go.Scatter(name = unique_link[i],x = link_coord_x[i],y = link_coord_y[i],mode = 'markers'))
    py.iplot(trace,filename = 'scatter_plot')
    return render_template('scatterplot_user.html')

@app.route("/piechart_user", methods=['POST','GET'])
def piechart_user():
    #csv = np.genfromtxt('aaamouse.csv',delimiter = ",")
    global new_session
    filename = new_session + ".csv"
    f = open(filename , 'a+')
    events = []
    link = []
    date =[]
    time =[]
    colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']
    reader = csv.reader(f,delimiter = ',')
    for row in reader:
        date .append(row[0])
        time.append(row[1])
        events.append(row[2])
        link.append(row[3])

    #unique_link = set(link)
    #unique_link = list(unique_link)

    #unique_events = set(events)
    #unique_events = list(unique_events)
        
    d = dict((x,events.count(x)) for x in set(events))
    print (d.keys(), file=sys.stderr)
    print (d.values(), file=sys.stderr)
    trace = go.Pie(labels=d.keys(), values=d.values(),
               hoverinfo='label+percent', textinfo='value', 
               textfont=dict(size=20),
               marker=dict(colors=colors, 
                           line=dict(color='#000000', width=2)))
    py.iplot([trace], filename='pie_chart')


    return render_template('piechart_user.html')

@app.route("/social", methods=['POST','GET'])
def social():
        return render_template('social.html') 


@app.route("/social_barchart", methods=['POST','GET'])
def social_barchart():
        cur=mysql.connection.cursor()
        cur.execute("""SELECT USERNAME FROM user_account""")
        t = cur.fetchall()
        t = list(t)
        users = []
        trace = []
        for a in t:
                #print(a,file = sys.stderr)
                (session,) = a
                filename = str(session) + ".csv"
                print (filename , file =sys.stderr)
                f = open(filename , 'a+')
                events = []
                link = []
                date =[]
                time =[]
                colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']
                reader = csv.reader(f,delimiter = ',')
                for row in reader:
                        date .append(row[0])
                        time.append(row[1])
                        events.append(row[2])
                        link.append(row[3])

    
        
                d = dict((x,events.count(x)) for x in set(events))
                trace.append (go.Bar(x=d.keys(),y=d.values(),text=d.values(),textposition = 'auto' , name = str(session)))
        py.iplot(trace, filename='social_barchart')
                
                
        return render_template('social_barchart.html')
@app.route("/social_barchart1", methods=['POST','GET'])
def social_barchart1():
        cur=mysql.connection.cursor()
        cur.execute("""SELECT USERNAME FROM user_account""")
        t = cur.fetchall()
        t = list(t)
        users = []
        trace = []
        count = {}
        for a in t:
                
                #print(a,file = sys.stderr)
                (session,) = a
                #count[session] = 0
                filename = str(session) + ".csv"
                print (filename , file =sys.stderr)
                f = open(filename , 'a+')
                events = []
                link = []
                date =[]
                time =[]
                colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']
                reader = csv.reader(f,delimiter = ',')
                for row in reader:
                        date .append(row[0])
                        time.append(row[1])
                        events.append(row[2])
                        link.append(row[3])
                d = dict((x,events.count(x)) for x in set(events))
                l = dict((x,link.count(x)) for x in set(link))
                #for 
                trace.append (go.Bar(x=l.keys(),y=l.values(),text=d.values(),textposition = 'auto' , name = str(session)))
        py.iplot(trace, filename='social_barchart1')
        return render_template('social_barchart1.html')

@app.route("/social_piechart", methods=['POST','GET'])
def social_piechart():
        cur=mysql.connection.cursor()
        cur.execute("""SELECT USERNAME FROM user_account""")
        t = cur.fetchall()
        t = list(t)
        users = []
        global count1
        count1 = {}
        for a in t:
                
                #print(a,file = sys.stderr)
                (session,) = a
                
                filename = str(session) + ".csv"
                print (filename , file =sys.stderr)
                f = open(filename , 'a+')
                events = []
                link = []
                date =[]
                time =[]
                colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']
                reader = csv.reader(f,delimiter = ',')
                for row in reader:
                        date .append(row[0])
                        time.append(row[1])
                        events.append(row[2])
                        link.append(row[3])
                d = dict((x,events.count(x)) for x in set(events))
                l = dict((x,link.count(x)) for x in set(link))
                #global count1
                count1[session] =  len(time)
                print (count1[session],file=sys.stderr)
                #for 
                #trace.append (go.Bar(x=l.keys(),y=l.values(),text=d.values(),textposition = 'auto' , name = str(session)))
        trace = go.Pie(labels=count1.keys(), values=count1.values() , name = str(session))        
        py.iplot([trace], filename='social_piechart')
        return render_template('social_piechart.html')



@app.route('/logging', methods=['GET'])
@cross_origin()
def logging():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == 'GET':
        global new_session    
        filename = new_session + " " +"user" +".log"
        filename1 = new_session + " " +"user"+ "_mouse_traj" + ".log"
        csv_filename = new_session + ".csv"
        csv_mouse = new_session + "mouse" + ".csv"
        csv_write = open(csv_filename,"a+")
        csv_write_mouse = open(csv_mouse,"a+")
        
        writer = csv.writer(csv_write, delimiter = ',')
        writer_mouse = csv.writer(csv_write_mouse, delimiter = ',')
        te = str(request.args.get('Message'))
        
        
        mess = str(timestamp) +  "   " +  te + "\n"
        d , t = timestamp.split(" ")
        
        if(te != "None" and "mouse movement trajectory:" not in te):
                
                m , link = te.split(",")
                writer.writerow((str(d),str(t),str(m) , str(link)))
                
                
        if("mouse movement trajectory:"  in te):
                m , link = te.split("--")
                
                me , axis = m.split(":")
                
                print (axis, file=sys.stderr)
                x,y = axis.split(",")
                x = x[3:]
                y = y[:-1]
                writer_mouse.writerow((str(d),str(t),str(x),str(y) , str(link)))
                
        csv_write_mouse.close()                
        csv_write.close()                
        return request.args.get('Message')
    
    return render_template('firstpage.html')

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
