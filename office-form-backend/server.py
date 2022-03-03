from flask import Flask, Response, request
import pymongo
import json 

app = Flask(__name__)
try:

    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017, 
        serverSelectionTimeoutMS = 1000
    )
    mongo.server_info()
    database = mongo.company
except Exception as ex :
    print("Cannot connect to database")



@app.route("/users", methods=['POST'])
def createUser():
    try: 
        user= {
        "name": request.form["name"], 
        "empid": request.form["empid"], 
        "designation":"Intern",
        "email" : "sbjoel112000@gmail.com",
        "firstPointOfContact": "brightons@karunya.edu.in",
        "secondPointOfContact": "sbytube112000@gmail.com"
        }
        dbResponse = database.users.insert_one(user)
        print(dbResponse.inserted_id)
        return Response(
            response= json.dumps(
                {"message":"User created!", 
                "id": f"{dbResponse.inserted_id}"
                }),
            status= 200,
            mimetype="application/json"

        )

    except Exception as ex:
        print(ex)
    return "False"

@app.route("/members")
def members():
    return {"member":["member1 ", "members2", "member3"]}

if __name__ == "__main__":
    app.run(debug=True)