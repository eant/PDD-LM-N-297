from flask import Flask, json, request
from pymongo import MongoClient
from urllib.parse import urlencode
import settings
from os import environ

USER = environ["DB_USER"]
PASS = environ["DB_PASS"]
HOST = environ["DB_HOST"]
BASE = environ["DB_NAME"]
PORT = environ["PORT"]
FLASK_ENV = environ["FLASK_ENV"]



app = Flask(__name__)

### MongoDB ###
config = {
    'retryWrites' : "true",
    'w' : "majority",
    'ssl' : "true",
    'ssl_cert_reqs' : "CERT_NONE"
}
client = MongoClient("mongodb+srv://" + USER + ":" + PASS + "@" + HOST + "/" + BASE + "?" + urlencode(config))
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
@app.route("/tweets/<path>")
def getTweets(path):
    twitter = client['PDD-MJ-N-287']['twitter']
    
    if path not in ['people', 'company']:
        result = { 'error' : 'Categoria no disponible' }
    else:
        users = twitter.find({ 'type' : path }).limit(4)
    
        result = []
    
        for user in users:
            item = {
                'usuario' : user['name']
            }
            result.append(item)
    
    return app.response_class(response = json.dumps(result), status  = 200, mimetype = "application/json" )

###############

###############
@app.route("/tweets", methods = ["POST"])
def newTweet():
    twitter = client['PDD-MJ-N-287']['twitter']
    
    ## ACA DEBERIA VALIDAR EL INGRESO DE DATOS ##
    
    tweet = {
        "id" : request.form["time"],
        "in_reply_to_screen_name" : request.form["user"],
        "full_text" : request.form["message"]
    }

    result = twitter.insert_one( tweet )
    
    if result.acknowledged == True:
        
        response = {
            "ok" : True,
            "msg" : "Tweet guardado correctamente :D"
        }

    else:
        
        response = {
            "ok" : False,
            "msg" : "Error al guardar el Tweet :("
        }
    
    return app.response_class(response = json.dumps(response), status  = 200, mimetype = "application/json" )




###############
if __name__ == "__main__":

    if FLASK_ENV == "development":
        
        app.run( port = PORT, host = "0.0.0.0" )
        
    else:
        
        app.run( port = PORT )
    
    
    
    
    
    
    