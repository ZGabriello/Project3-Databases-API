from neo4j import GraphDatabase

driver = GraphDatabase.driver('bolt://0.0.0.0:7687',
                              auth=('neo4j', 'neo4j'))

# deleting data
print('Deleting previous data')

query = '''
MATCH (n)
DETACH DELETE n
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')

# inserting data
print('Inserting nodes')

query = '''
LOAD CSV WITH HEADERS FROM 'https://github.com/ZGabriello/Project3-Databases-API/blob/main/nodes.csv' AS row
CREATE (:Node {name: row.node, type: row.type});
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')

print('Inserting edges')

query = '''
LOAD CSV WITH HEADERS FROM 'https://github.com/ZGabriello/Project3-Databases-API/blob/main/edges.csv' AS row
CREATE (:Edge {hero: row.hero, comic: row.comic});
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')

print('Creating relationships')

query = '''
LOAD CSV WITH HEADERS FROM 'https://github.com/ZGabriello/Project3-Databases-API/blob/main/hero-network.csv' AS row
MATCH (n:Node) WHERE n.name = row.hero1
MATCH (e:Edge) WHERE e.hero_name = row.hero2
CREATE (n)-[:APPEAR_IN]->(e)
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')
