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
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/ZGabriello/Project3-Databases-API/main/hero.csv' AS row
CREATE (:Hero {name: row.node});
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')

print('Inserting Comics')

query = '''
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/ZGabriello/Project3-Databases-API/main/comic.csv' AS row
CREATE (:Comic {name: row.node});
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')

print('Inserting Edges')

query = '''
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/ZGabriello/Project3-Databases-API/main/edges.csv' AS row
CREATE (:Edge {hero: row.hero, comic: row.comic});
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')

#print('Inserting Hero_Network')

#query = '''
#LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/ZGabriello/Project3-Databases-API/main/hero-network.csv' AS row
#CREATE (:Hero_Network {hero1: row.hero1, hero2: row.hero2});
#'''

#with driver.session() as session:
#    print(query)
#    session.run(query)

#print('done')

print('Creating Relationships')

query = '''
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/ZGabriello/Project3-Databases-API/main/edges.csv' AS row
MATCH (h:Hero) WHERE h.name = row.hero
MATCH (c:Comic) WHERE c.name = row.comic
CREATE (h)-[:APPEAR_IN]->(c);
'''

with driver.session() as session:
    print(query)
    session.run(query)

print('done')
