# Project3-Databases-API

# Description

L’objectif de ce projet est de choisir, mettre en place, et peupler une base de données à partir d’un jeu de données de l’open data, et d’implémenter une API permettant de requêter cette base de données.

# Data 

Le data choisit pour ce projet est : https://www.kaggle.com/csanhueza/the-marvel-universe-social-network.
Ce sont des données qui sont orientées graphes donc on va plutôt s'orienter vers Neo4J pour le choix du BDD que l'on va utiliser.

# Utilisation 

# Neo4j
Pour commencer, il faut lancer le docker Neo4j avec la commande :

docker container run -p 7474:7474 -p 7687:7687 datascientest/neo4j

On pourra ainsi accéder à Neo4j sur l'adresse "localhost:7474" ou "adresse_ip_vm:7474" avec comme nom d'utilisateur "neo4j" et mot de passe "neo4j" 

# Script de chargement des données 
Nous avons un script python qui va lancer le chargement des données dans la base de données de Neo4j pour cela il suffit de faire la commande suivante depuis le répertoire contenant le script "load_data_into_neo4j_database.py" : 

python3 load_data_into_neo4j_database.py

# API Flask 

Pour accéder à l'API Flask, il faudra lancer les commandes suivantes : 

export FLASK_APP=app.py 

export FLASK_ENV=development

flask run --host=0.0.0.0

On pourra ainsi accéder à l'api sur l'adresse "localhost:5000" ou "adresse_ip_vm:5000" 
