from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello1():
	return "my name is ttt"

@app.route("/name")
def hello():
	return "my name is"
	
@app.route("/name/<name>")
def name(name):
	return "my name is"+ name
	
@app.route("/firstname", methods =["GET"])
def get():
	var = request.args.get("firstname")
	return var
	
if __name__ == "__main__":
	app.run()

