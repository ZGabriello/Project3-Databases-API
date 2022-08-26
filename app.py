from flask import Flask
from flask import request
from neo4j import GraphDatabase

app = Flask(__name__)

// Neo4j database 
driver = GraphDatabase.driver("bolt://52.48.111.88:7687", auth=basic_auth("neo4j", "neo4j"))
driver = GraphDatabase.driver(uri="bolt://52.48.111.88:7687", auth=("neo4j", "neo4j"))
session = driver.session()

query = """
match (n:Hero) return n.name as name limit 10
"""
results = session.run(query)

for result in results:
    print(result["name"])

@app.route("/")
def welcome():
    return "<h1> Welcome to the API that manage requests to our Neo4J BDD !  </h1>"

@app.route("/heroes")
def list_heroes():
    return "La liste des heros de comics est : {}".format(results)
  
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
