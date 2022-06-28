from curses import flash
from imp import reload
from flask import Flask
import importlib 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> <h1> Brighton </h1>"

app.run(debug=True, use_reloader= True)