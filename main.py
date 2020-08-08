from flask import Flask, render_template, request
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

codesjson = requests.get("http://codehive.sketchub.in/api/", headers = headers)
codes = json.loads(codesjson.content)

for c in range(len(codes)):
    codes[c]["id"] = c

app = Flask('app')

@app.route('/', methods=["GET","POST"])
def main():
    if request.args.get("search"):
        key_words = request.args.get("search").split(" ")
        return render_template("search.html", search=request.args.get("search"), key_words = key_words, data=codes)
    else:
        return render_template("index.html", data=codes, )

@app.route("/view/<id>")
def view_code(id):
    return render_template("view.html", data=codes, id=int(id))

@app.route("/ping")
def ping():
    return "pinged"

app.run(host='0.0.0.0', port=8080)