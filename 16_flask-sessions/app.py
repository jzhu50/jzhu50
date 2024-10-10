'''
Michelle, Ryan, Linda
Boas
SoftDev
K16 -- flask_sessions
2024-10-11
time spent: 0.5
'''

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
# app.secret_key = "haha"

@app.route("/")
def disp_loginpage():
    user_id = request.cookies.get('MyCookie')
    return render_template( 'login.html' )

@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    username = request.form['username'] if request.method == 'POST' else request.args.get('username')
    app.set_cookie('MyCookie', user_id)
    cookie = request.cookies.get('MyCookie')
    return render_template( 'response.html', name = username)

@app.route("/out")
def disp_logoutpage():
    request.cookies.pop('MyCookie')
    return render_template( 'logout.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()