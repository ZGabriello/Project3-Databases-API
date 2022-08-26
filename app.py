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
    match (h:Hero) return h.name as name 
    """
    results = session.run(query)
    data = []
    for result in results:
        data.append(result["name"])
    return """
        <h3> La liste des heros de comics est : </h3>
        {}
        """.format(data)

@app.route("/comics")
def list_comics():
    query = """
    match (c:Comic) return c.name as name 
    """
    results = session.run(query)
    data = []
    for result in results:
        data.append(result["name"])
    return """
        <h3> La liste des comics est : </h3>
        {}
        """.format(data)
  
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
