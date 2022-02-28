from flask import Flask
import pymongo

try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port="27017",
        serverSelectionTimeoutMS = 1000
    )
    mongo.server_info()

    database = mongo.company
except Exception as ex :
    print(ex)

app = Flask(__name__)

@app.route("/users")
def createUser():
    try:
        
    except Exception as ex:
        print(ex)

@app.route("/members")
def members():
    return {"member":["member1 ", "members2", "member3"]}

if __name__ == "__main__":
    app.run(debug=True)