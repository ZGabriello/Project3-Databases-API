from flask import Flask
from flask import request
from neo4j import GraphDatabase

app = Flask(__name__)

driver = GraphDatabase.driver(uri="bolt://52.48.111.88:7687", auth=("neo4j", "neo4j"))
session = driver.session()

@app.route("/")
def welcome():
    return "<h1> Welcome to the API that manage requests to our Neo4J BDD !  </h1>"

@app.route("/heroes")
def list_heroes():
    query = """
    match (n:Hero) return n.name as name limit 10
    """
    results = session.run(query)
    for result in results:
        return """
        La liste test des heros de comics est :
        """.format(result["name"])
  
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
