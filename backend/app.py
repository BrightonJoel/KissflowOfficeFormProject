from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "<p>Hello, World!</p> <h1 style='color: red;'> Brighton </h1>"


@app.route("/login")
def login():
    return "<h1> This is a sample login page from backend </h1>"

@app.route("/register")
def register():
    return "<h1> This is a sample register page from backend </h1>"

@app.route("/admin")
def admin():
    return "<h1> This is a sample admin page from backend </h1>"

@app.route("/manager")
def manager():
    return "<h1> This is a sample manager page from backend </h1>"

@app.route("/employee")
def employee():
    return "<h1> This is a sample employee page from backend </h1>"


app.run(debug=True, use_reloader= True)