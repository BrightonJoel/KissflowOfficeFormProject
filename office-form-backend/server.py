from flask import Flask

app = Flask(__name__)

@app.route("/members")
def members():
    return {"member":["member1 ", "members2", "member3"]}

if __name__ == "__main__":
    app.run(debug=True)