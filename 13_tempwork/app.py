'''
Michelle Zhu, Linda Zheng
ducky123
SoftDev
<K13> -- tempwork
2024-09-30
time sepnt:
'''

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/wdywtbwygp")

def tmplt():
    return render_template("tablified.html", title = "foo")

if __name__ == "__main__":
    app.debug = True
    app.run()
