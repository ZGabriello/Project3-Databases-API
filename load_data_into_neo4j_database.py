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

print('Inserting edges')

query = '''
LOAD CSV WITH HEADERS FROM 'https://github.com/ZGabriello/Project3-Databases-API/blob/d1535dfe3bc047326e5c264b1a5249798f3120e9/edges.csv' AS row
CREATE (:Edge {hero: row.hero, comic: row.comic});
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')

print('Inserting hero_network')

query = '''
LOAD CSV WITH HEADERS FROM 'https://github.com/ZGabriello/Project3-Databases-API/blob/0d8ddaa6365fb10974d9c5cf9e3d0f09962e552f/hero-network.csv' AS row
CREATE (:Same_comic {hero1: row.hero1, hero2: row.hero2});
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')

print('Creating Relationships')

query = '''
LOAD CSV WITH HEADERS FROM 'https://github.com/ZGabriello/Project3-Databases-API/blob/d1535dfe3bc047326e5c264b1a5249798f3120e9/edges.csv' AS row
MATCH (e:Edge) WHERE e.hero = row.hero
MATCH (n:Node) WHERE n.name = row.comic
CREATE (e)-[:APPEAR_IN]->(n);
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')
