from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> <h1 style='color: red;'> Brighton </h1>"




app.run(debug=True, use_reloader= True)