'''
Michelle, Ryan, Linda
Boas
SoftDev
K18 -- livestuyle
2024-10-16
time spent: 0.5
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page():
    return render_template('index.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()