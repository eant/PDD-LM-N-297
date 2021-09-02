from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola mundo desde la home de <b>Flask</b> :D"


app.run( port = 3000, host = "0.0.0.0" )