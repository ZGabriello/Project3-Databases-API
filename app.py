from flask import Flask
from flask import request

app = Flask(__name__)

// Neo4j database 
driver = GraphDatabase.driver("bolt://52.48.111.88:7687", auth=basic_auth("neo4j", "neo4j"))


@app.route("/")
def welcome():
    return "<h1> Welcome to the API that manage requests to our Neo4J BDD !  </h1>"
  
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
