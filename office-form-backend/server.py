from flask import Flask, Response, request
import pymongo
import json 
import timestring
import dateutil.parser
from flask_cors import CORS
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
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



@app.route("/api/leaveFormSubmit", methods=['POST'])
def createLeaveForm():
    try: 
        print(request.json["empid"],request.json["email"],
        request.json["fromdate"],request.json["todate"])
        form= {
        "empid": int(request.json["empid"]), 
        "email": request.json["email"], 
        "fromdate": dateutil.parser.isoparse(request.json["fromdate"]),
        "todate": dateutil.parser.isoparse(request.json["todate"]),
        "reason" : request.json["reason"]
        }
        dbResponse = database.forms.insert_one(form)
       

        user = database.users.find_one({"empid": int(request.json["empid"])})
        user = json.load(user)
        s = Serializer('WEBSITE_SECRET_KEY', 60*30) # 60 secs by 30 mins
        token = s.dumps(
            {'user_name':user['name'] ,
            'user_designation': user['designation'],
            'user_empid': user['empid'],
            'user_email': user['email'],
            'form_to_date': form['todate'],
            'form_reason' : form['reason'],
            'form_from_date':form['fromdate']}).decode('utf-8')
        print(url_for('get_file', token=token))
        return Response(
            response= json.dumps(
                {"message":"Form submitted and the email is sent", 
                "id": f"{dbResponse.inserted_id}"
                }),
            status= 200,
            mimetype="application/json"

        )

    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps(
                {"message": str(ex)
                }),
            status= 400,
            mimetype="application/json"

        )

@app.route("/members")
def members():
    return {"member":["member1 ", "members2", "member3"]}

if __name__ == "__main__":
    app.run(debug=True)