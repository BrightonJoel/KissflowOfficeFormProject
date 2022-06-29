from flask import Flask, jsonify, make_response, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from functools import wraps
import datetime
import secrets
from queries import Employee
import json
import uuid
import jwt


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)


###########################################################################################################
# Functions
############################################################################################################

def authenticate(username: str, password: str) -> bool:
    if username == "Brighton" and password == "1234":
        return True
    return False

###########################################################################################################
# Routes
############################################################################################################

@app.route("/")
def helloWorld():
    return "<p>Hello, World!</p> <h1 style='color: red;'> Brighton </h1>"


@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        if authenticate(request.form['username'], request.form['password']):
            return json.dumps({"message": request.form['username'] + " was logged in"})
    else:
        return "<h1> This is a sample login page from backend </h1>"


@ app.route("/register", methods=["GET"])
def register():
    return Employee(empName = "Brighton", empPassword = "Admindznk@68901", empPosition = "Admin").createEmployee()


@ app.route("/admin")
def admin():
    return "<h1> This is a sample admin page from backend </h1>"


@ app.route("/manager")
def manager():
    return "<h1> This is a sample manager page from backend </h1>"


@ app.route("/employee")
def employee():
    return "<h1> This is a sample employee page from backend </h1>"


app.run(debug=True, use_reloader=True)
