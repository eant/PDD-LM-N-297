from flask import Flask, json

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola mundo desde la home de <b>Flask</b> :D"


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

app.run( port = 3000, host = "0.0.0.0" )