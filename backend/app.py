from imp import reload
from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> <h1 style='color: red;'> Brighton </h1>"


@app.route("/products")
def products():
    products = ["Socks", "Shoes", "Shirts"]
    return json.dumps(products)

@app.route('/product/<int:num>', methods = ['GET'])
def product(num):
    products = ["Socks", "Shoes", "Shirts"]
    return json.dumps(products[num])


app.run(debug=True, use_reloader= True)