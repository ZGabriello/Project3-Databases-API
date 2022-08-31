# Project3-Databases-API

# Description

L’objectif de ce projet est de choisir, mettre en place, et peupler une base de données à partir d’un jeu de données de l’open data, et d’implémenter une API permettant de requêter cette base de données.

# Data 

Le data choisit pour ce projet est : https://www.kaggle.com/csanhueza/the-marvel-universe-social-network.
Ce sont des données qui sont orientées graphes donc on va plutôt s'orienter vers Neo4J pour le choix du BDD que l'on va utiliser.
En effet, Neo4j est pour moi sur ce dataset le meilleur choix de base de données au vu des fichiers csv qu'on a et des relations entre les noeuds. 

# Utilisation 

# Neo4j
Pour commencer, il faut lancer le docker Neo4j avec la commande :

docker container run -p 7474:7474 -p 7687:7687 datascientest/neo4j

On pourra ainsi accéder à Neo4j sur l'adresse "localhost:7474" ou "adresse_ip_vm:7474" avec comme nom d'utilisateur "neo4j" et mot de passe "neo4j" 

# Script de chargement des données 
Nous avons un script python qui va lancer le chargement des données dans la base de données de Neo4j pour cela il suffit de faire la commande suivante depuis le répertoire contenant le script "load_data_into_neo4j_database.py" : 

python3 load_data_into_neo4j_database.py

A noter : Le chargement des données mets du temps, surtout pour la mise en place des relations entre les heros et les comics.

# API Flask 

Pour accéder à l'API Flask, il faudra lancer les commandes suivantes : 

export FLASK_APP=app.py 

export FLASK_ENV=development

flask run --host=0.0.0.0

On pourra ainsi accéder à l'api sur l'adresse "localhost:5000" ou "adresse_ip_vm:5000" 

Les routes disponible sont : 

/ : Page d'accueil 

/heroes : Permet d'accéder à la liste de héros de comic de la base de données 

/comics : Permet d'accéder à la liste de comics de la base de données 

/hero_appearing_in_comic : Permet d'accéder à la liste de héros et de comics dans lequel ils apparaisent de la base de données 

/add_hero : Permet d'ajouter un hero à la liste de héros de comic de la base de données 
Pour cela il faut ouvrir le html correspondant au formulaire d'ajout

/add_comic : Permet d'ajouter un comic à la liste de comic de la base de données 
Pour cela il faut ouvrir le html correspondant au formulaire d'ajout

/delete_hero : Permet de supprimer un hero de la liste de héros de comic de la base de données 
Pour cela il faut ouvrir le html correspondant au formulaire d'ajout

/delete_comic : Permet de supprimer un comic de la liste de comic de la base de données 
Pour cela il faut ouvrir le html correspondant au formulaire d'ajout

# Docker 

Un potentiel docker compose pour lancer le docker de Neo4j, le script de chargement de données et lancer flask serait intéressant pour ce projet.
