from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1> Welcome to the API that manage requests to our Neo4J BDD !  </h1>"
  
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
