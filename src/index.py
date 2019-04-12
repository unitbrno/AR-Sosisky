from flask import Flask
app = Flask(__name__)

with open('./index.html', 'r') as f:
    l = f.read()


print(l)

@app.route("/index.html")
def index():
    return l

@app.route("/tasks.html")
def open():
    pass


#@app.route("/warnings.html")


#@app.route("/both.html")

