from flask import Flask
app = Flask(__name__)

with open('index.html', 'r') as f:
    l1 = f.read()

with open('tasks.html', 'r') as f:
    l2 = f.read()

with open('warnings.html', 'r') as f:
    l3 = f.read()

with open('both.html', 'r') as f:
    l4 = f.read()


@app.route("/index.html")
def index():
    return l1

@app.route("/tasks.html")
def opes():
    return l2

@app.route("/warnings.html")
def oper():
    return l3

@app.route("/both.html")
def oden():
    return l4


#@app.route("/warnings.html")


#@app.route("/both.html")

