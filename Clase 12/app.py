from flask import Flask, json
from pymongo import MongoClient
app = Flask(__name__)

### MongoDB ###
client = MongoClient("mongodb+srv://eant-python:eantpass2021@python-data-developers.osipp.mongodb.net/PDD-MJ-N-287?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
###############

###############
@app.route("/")
def home():
    return "Hola mundo desde la home de <b>Flask</b> :D"
###############

###############
@app.route("/users")
def usersTwitter():
    users = [
        { "name" : "smessina_" },
        { "name" : "eanttech" },
        { "name" : "TinchoLutter" },
        { "name" : "bitcoinarg" }
    ]
    
    response = app.response_class(response = json.dumps(users), status = 200, mimetype = "application/json")

    return response
###############

###############
@app.route("/tweets")
def getTweets():
    twitter = client['PDD-MJ-N-287']['twitter']
    
    users = twitter.find().limit(4)
    
    result = []
    
    for user in users:
        item = {
            'usuario' : user['name']
        }
        result.append(item)
    
    return app.response_class(response = json.dumps(result), status  = 200, mimetype = "application/json" )












###############

app.run( port = 3000, host = "0.0.0.0" )