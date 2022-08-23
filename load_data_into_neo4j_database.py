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
LOAD CSV WITH HEADERS FROM 'https://github.com/ZGabriello/Project3-Databases-API/blob/a4c5f0933cae4d896a04bcf4e178db2a735166f8/nodes.csv' AS row
CREATE (:Node {name: row.node, type: row.type});
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')

print('Inserting heroes')

query = '''
LOAD CSV WITH HEADERS FROM 'https://github.com/ZGabriello/Project3-Databases-API/blob/a4c5f0933cae4d896a04bcf4e178db2a735166f8/nodes.csv' AS row
MATCH (n:Node) WHERE n.type CONTAINS "hero"
CREATE (:Hero {name: n.node});
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')

print('Inserting comics')

query = '''
LOAD CSV WITH HEADERS FROM 'https://github.com/ZGabriello/Project3-Databases-API/blob/a4c5f0933cae4d896a04bcf4e178db2a735166f8/nodes.csv' AS row
MATCH (n:Node) WHERE n.type CONTAINS "comic"
CREATE (:Comic {name: n.node});
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')

print('Inserting edges')

query = '''
LOAD CSV WITH HEADERS FROM 'https://github.com/ZGabriello/Project3-Databases-API/blob/d1535dfe3bc047326e5c264b1a5249798f3120e9/edges.csv' AS row
CREATE (:Edge {hero: row.hero, comic: row.comic});
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')

