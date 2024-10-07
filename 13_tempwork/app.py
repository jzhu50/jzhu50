'''
Michelle Zhu, Linda Zheng
ducky123
SoftDev
<K13> -- tempwork
2024-09-30
time sepnt: 0.5
'''

from flask import Flask, render_template
import random
app = Flask(__name__)

def occupations_dict():
    occupations_str = open('data/occupations.csv').read()
    print(occupations_str)
    records = occupations_str.split('\n')
    records.pop(0)
    records.pop(-1) 
    records.pop(-1)

    occupations_info = {}
    
    for record in records:
        occupation, percentage = record.rsplit(',', 1)
        occupation = occupation.replace('"',' ') # get rid of quotation marks
        occupations_info[occupation] = float(percentage)
    return occupations_info

def table():
    occupations = occupations_dict()
    head = "<table><tr><th>Job Class</th><th>Percentage</th><th>Link</th><tr>"
    body = ""
    for i in occupations:
        body += "<tr><td>" + i + "</td><td>" + str(occupations[i]) + "</td></tr>"
    output = head + body + "</table>"
    return output

# select occupations 100 times based on the percentage weights
def random_selection(occupations_info, num):
    occupations = list(occupations_info.keys())
    percentages = list(occupations_info.values())
    return random.choices(occupations, weights=percentages, k=num)

@app.route("/")
def main():
    return "head to /wdywtbwygp"

@app.route("/wdywtbwygp")
def tmplt():
    return render_template("tablified.html", title = "13_combine", table = table(), occupation = random_selection(occupations_dict(),1))

if __name__ == "__main__":
    app.debug = True
    app.run()