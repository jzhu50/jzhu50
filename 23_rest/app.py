from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__)

with open("key_nasa.txt", "r") as f:
    api_key = f.read().strip()
    
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

data = urllib.request.urlopen(url) # opens a network connection to the URL and fetches the raw data
print(data) # returns a HTTPResponse
print(data.geturl()) # returns url
print(data.info()) # returns header info

data = data.read() # returns page source code
data_json = json.loads(data)
print(data_json) # turns a JSON object string into a dictionary
# json.dumps() # turns python dict into JSON object string
print(data_json.get("explanation"))

@app.route("/")
def home():
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    
    image_url = data.get("url")
    explanation = data.get("explanation")
    title = data.get("title", "Astronomy Picture of the Day")
    
    TNPG = "dualbeans"
    roster = "Michelle, Ivan"
    
    return render_template("main.html",
                           team_name=TNPG, 
                           roster=roster, 
                           title=title, 
                           image_url=image_url, 
                           explanation=explanation)

if __name__ == "__main__":
    app.run(debug=True)
