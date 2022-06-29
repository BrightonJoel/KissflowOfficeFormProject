from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, make_response, request
from flask_pymongo import PyMongo
from functools import wraps

import datetime
import secrets
import hashlib
import json


"""
Custom packages
"""
from queries import Employee

"""
flask object
"""
app = Flask(__name__)

"""
JWT TOKEN Configuration
"""
jwt = JWTManager(app)  # initialize JWTManager
app.config['JWT_SECRET_KEY'] = secrets.token_hex(16)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

###########################################################################################################
# Functions
############################################################################################################


def sampleFuction():
    pass
###########################################################################################################
# Routes
############################################################################################################


@app.route("/")
def helloWorld():
    return "<p>Hello, World!</p> <h1 style='color: red;'> Brighton </h1>"


@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        # store the json body request meaning raw json file
        loginUser = json.loads(request.get_data())

        currentLoggingUser = Employee(
            empName=loginUser["username"]).findOneEmployee()

        if currentLoggingUser:
            # encrpting the entered password for check
            encrpted_password = hashlib.sha256(
                loginUser['password'].encode("utf-8")).hexdigest()

            if encrpted_password == currentLoggingUser['empPassword']:
                # creating Json Web Token
                access_token = create_access_token(
                    identity=currentLoggingUser['empName'])
                return jsonify(access_token=access_token), 200

        return jsonify({'msg': 'The username or password is incorrect'}), 401
    else:
        return "<h1> This is a sample login page from backend </h1>"


@app.route("/register", methods=["POST"])
def register():
    newUserData = json.loads(request.get_data())
    newUserData["password"] = hashlib.sha256(
        newUserData["password"].encode("utf-8")).hexdigest()
    newUser = Employee(
        empName=newUserData["username"], empPassword=newUserData["password"])

    if not newUser.findOneEmployee():
        statusInfo = newUser.createEmployee()
        if statusInfo["CreationStaus"]:
            return jsonify({"message":statusInfo["MongoMessage"]}), 200 #Success
        else:
            return jsonify({"message":statusInfo["MongoMessage"]}), 502 #database Error
    else:
        return jsonify({"message": "user exists"}), 409 #Already exists


@app.route("/admin", methods=["GET"])
@jwt_required
def admin():
    # Getting the user via the JWT
    currentUser = get_jwt_identity()
    
    employeeInstanceFromDb = Employee(empName=currentUser).findOneEmployee()

    if employeeInstanceFromDb:
        return jsonify({"message" : "User successfully authenticated from admin", 
        "userInstance" : employeeInstanceFromDb}), 200
    
    else:
        return jsonify({"message" : "Well someone is skeaking around 😒😒. 🦖💨💨"}), 404


@app.route("/manager")
def manager():
    return "<h1> This is a sample manager page from backend </h1>"


@app.route("/employee")
def employee():
    return "<h1> This is a sample employee page from backend </h1>"


app.run(debug=True, use_reloader=True)
