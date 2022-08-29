from flask import Flask, redirect, url_for
from flask import request
from neo4j import GraphDatabase

app = Flask(__name__)

driver = GraphDatabase.driver(uri="bolt://52.48.111.88:7687", auth=("neo4j", "neo4j"))
session = driver.session()

@app.route("/")
def welcome():
    return "<h1> Welcome to the API that manage requests to our Neo4J BDD !  </h1>"

@app.route('/success/<name>')
def success(name):
   return 'On a bien ajouté %s à la base' % name

@app.route('/deleted/<name>')
def deleted(name):
   return 'On a bien supprimé %s à la base' % name

@app.route("/heroes")
def list_heroes():
    query = """
    match (h:Hero) return h.name as name 
    """
    results = session.run(query)
    compteur = 0 
    index = []
    data = []
    resultat = {}
    for result in results:
        index.append(compteur)
        data.append(result["name"])
        compteur = compteur + 1 
    for i in range(len(data)):
        resultat[index[i]] = data[i]
    return """
        <h3> La liste des heros de comics est : </h3>
        {}
        """.format(resultat)

@app.route("/comics")
def list_comics():
    query = """
    match (c:Comic) return c.name as name 
    """
    results = session.run(query)
    data = []
    compteur = 0 
    index = []
    resultat = {}
    for result in results:
        index.append(compteur)
        data.append(result["name"])
        compteur = compteur + 1 
    for i in range(len(data)):
        resultat[index[i]] = data[i]
    return """
        <h3> La liste des comics est : </h3>
        {}
        """.format(resultat)

@app.route("/hero_appearing_in_comic")
def hero_and_comic():
    query = """
    match (n)-[:APPEAR_IN]->(p) return n.name as hero,p.name as comic limit 200
    """
    results = session.run(query)
    data = {}
    hero = []
    comic = [] 
    for result in results:
        hero.append(result["hero"])
        comic.append(result["comic"])
    for i in range(len(hero)):
        data[hero[i]] = comic[i]
    return """
        <h3> La liste des heros apparaissant dans un comic est : </h3>
        {}
        """.format(data)

@app.route("/add_hero", methods = ["POST", "GET"])
def add_new_hero():
    if request.method == 'POST':
        hero_name = request.form["hero"]
        query = """
        CREATE (h:Hero {name:$name}) return h.name as hero
        """
        x = {'name': hero_name}
        results = session.run(query, x)
        return redirect(url_for('success',name = hero_name))
    
@app.route("/add_comic", methods = ["POST", "GET"])
def add_new_comic():
    if request.method == 'POST':
        comic_name = request.form["comic"]
        query = """
        CREATE (c:Comic {name:$name}) return c.name as comic
        """
        x = {'name': comic_name}
        results = session.run(query, x)
        return redirect(url_for('success',name = comic_name))

@app.route("/delete_hero",methods=["DELETE"])
def delete_hero():
    if request.method == 'DELETE':
        hero_name = request.form["hero"]
        query = """
        MATCH (h:Hero {name:$name}) DETACH DELETE h
        """
        x = {'name': hero_name}
        results = session.run(query, x)
        return redirect(url_for('deleted',name = hero_name))

@app.route("/delete_comic",methods=["DELETE"])
def delete_comic():
    if request.method == 'DELETE':
        comic_name = request.form["comic"]
        query = """
        MATCH (c:Comic {name:$name}) DETACH DELETE c
        """
        x = {'name': comic_name}
        results = session.run(query, x)
        return redirect(url_for('deleted',name = comic_name))
  
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
