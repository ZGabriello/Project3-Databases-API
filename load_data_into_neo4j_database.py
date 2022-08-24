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
print('Inserting heroes')

query = '''
LOAD CSV WITH HEADERS FROM 'https://github.com/ZGabriello/Project3-Databases-API/blob/4eda7574890aca72f304a7e7a874da2715208a40/hero.csv' AS row
CREATE (:Hero {name: row.node});
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')

print('Inserting Comics')

query = '''
LOAD CSV WITH HEADERS FROM 'https://github.com/ZGabriello/Project3-Databases-API/blob/4eda7574890aca72f304a7e7a874da2715208a40/comic.csv' AS row
CREATE (:Comic {name: row.node});
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
MATCH (h:Hero) WHERE h.name = row.hero
MATCH (c:Comic) WHERE c.name = row.comic
CREATE (h)-[:APPEAR_IN]->(c);
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')
