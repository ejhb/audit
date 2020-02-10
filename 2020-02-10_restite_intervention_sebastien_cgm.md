# Sebastien CMA CGM département des finance 


Est rentré dev data

L'outil qu'il utilise met en place un système de facturation maritime 

finalité d'un outil précédent 2 prototype sur un durée de 10 ans pour claim toute les autorisations puis avant ça prouvé que leur outils va fonctionné. Commencé à 4 finis a 16 personne.
Partiellement en place depuis 2015.   

## SGBD : 
    
    - stockage : 
                - modéliser un métier 
                - stocker des données de façon typée et structurée 
                - gerer les écritures multiples et concurrentes

    - Intégrité ! 
                - Garantir la qualité des données 
                - Garantir l'application de règles métiers 
    
    - Restitution :
                - Récupérer / afficher des données sous une forme souhaitée 
                - Garantir la justesse des données renvoyées 

## Base de données : Les principaux Objets 
    
    - Tables 
    
    - Contraintes (PK ? SK, contraintes personalisées)
    
    - Vues / Vues matérialisées  Les vues temporaire qui seront pas stocké puis les vue maétrialisées "AS"
    
    - Index Une table vas être lu de manière linéaire tandis qu'une column indéxé sera lu comme une arboréscence
    
    - Trigger(& séquences)
    Language propriétaire la plus par du temps, 
    
    - Package / procédures stockées / Fonctions stockées 
    Package : regroupe plusieurs fonction/procédure
    
    - Types 
    Métadonnées : string / num ect. mais aussi créé un propre type de métadonnées
    
    - DB links
    Lié une base de données à une autre 

## SQL : Structured Query Language

    - Langage permettant d'exploiter une base de données (Lexture & Ecriture)
    
    - Langage de 4ème génération (mais n'est pas un langage objet)
    
    - langage serveur (vs langage client)
    
    - permet de manipuler des objets BDD avec des prédicats (éaglités/inégalités), des opérateurs logique (ET/OU)et mathématique 
    
    - Manipulation des lois ensemblistes :
        - Union 
        - Intersextions /existence 
        - Différence 
        - Produit cartésien (plus rare)

    - Permet d'agréger les données 
    
    - Fonction d'agréggations : si je veux récupéré des sommes ect.
    
    - Permet la transformation des données < à la volées > (règles conditionnelles, pivots , opération mathématiques)
    Pivots : interchangé les colum avec les lignes

## SQL : Jointures et lois ensemblistes : Les pouvoir de la patate!

Diapo

## SQL : Transformer des données 

    - Une requête < SELECT > : C'est une boucle!
    
    - Projections conditionnées (CASE WHEN) Les projections sont les tables qu'on selectionne.
    
    - Les sous-rêquetes
    
    - Les blocs < WITH > Le with permet de renomé une sous-requête. SELECT * FROM WITH SELECT * FROM plutôt qu'une UNION pour ainsi rappeler notre sous requête sans avoir à la retapé. 
    
    - Le tri (ORDER BY) Les tri sont très couteux en ressources, autant récupéré les données brut pour ensuite les trié. 
    
    - Utiliser des fonctions (formatage, conversion de type, manipulation de chaines)

## SQL : Agrégation des données 
  
    - Sommes (SUM)
    - Moyennes(AVG)
    - Minimum (MIN)
    - Maximum (MAX)
    - Concaténation (selon SGBD)
    - Une fonction d'agrégation oblige à toujours utiliser le regroupement (GROUP BY)
    
    - Prédicats sur le résultat d'agréation (HAVING)
    a having et toujours précédé d'un ORDER BY
    
    - Anttetion aux doublons : ; Comment gérer les agréagations avec cardinalité multiple 

## SQL : Quelques conseil / bonne pratique

    -  Ecrire les requêtes en < Colonne >
    - Indenter chaque sous-requêtes
    -  Utiliser dans Alias (table et colonnes)
    - WHERE 1=1 
    Permet de commenté les conditions de WHERE 
    
    - La virgule d'abord
    - Le < DISTINCT >
    Eviter le distinct, si on est obligé de sortir un distinct c'est que la requête manque d'optimisation.
    
    - Conditions multiples de jointures

## SQL : Aller plus loin avec ORACLE 

    - Le fenêtrage (windowing) : KEEP,DENSE_RANK,RANK,PARTITION BY, ect.
    - Optimisation et plan d'exécution 
    - Data statistics 
    - Les < Hint>
    - Le cace serveur 
    - les langages SGBD (PL/SQL)
    - Interroger des métadonnées 
    - Schedulers/Jobs


