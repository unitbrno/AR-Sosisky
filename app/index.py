from flask import Flask
from flask import render_template

app = Flask(__name__)


"""
with open('index.html', 'w') as f:
    l1 = f.read()

with open('tasks.html', 'w') as f:
    l2 = f.read()

with open('warnings.html', 'w') as f:
    l3 = f.read()

with open('both.html', 'w') as f:
    l4 = f.read()
"""

@app.route("/index.html")
def index():
    return render_template('index.html')


@app.route("/tasks.html")
def opes():
    return render_template('tasks.html')

@app.route("/warnings.html")
def oper():
    return render_template('warnings.html', data=['kokos', 'data'])

@app.route("/both.html")
def oden():
    return render_template('both.html')


#@app.route("/warnings.html")


#@app.route("/both.html")

