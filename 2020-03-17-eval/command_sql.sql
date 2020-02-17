-- Créer une base de données « RNE »
CREATE DATABASE RNE;

USE RNE;

-- 4. Y créer les tables destinées à accueillir les six fichiers cités plus haut. A vous de bienchoisir la longueur des champs et les types adéquate. Utilisez pour noms de colonnesceux renvoyer par r_names(). Le nom des tables doit être :
-- - elus
-- - population (La colonne population doit être en numérique)
-- - nuancier
-- - villes
-- - categorie (Les colonnes doivent être numérique)
-- - departements


-- TABLE CREATION:
-- Create Table elus creation
DROP TABLE IF EXISTS elus;
CREATE TABLE elus(
code_insee INT(7)
,mode_de_scrutin VARCHAR(1000)
,numliste INT(2)
,code_nuance_de_la_liste VARCHAR(6)
,numéro_du_candidat_dans_la_liste INT(4)
,tour INT(3)
,nom VARCHAR(1000)
,prénom VARCHAR(1000)
,sexe VARCHAR(1)
,data_de_naissance VARCHAR(10)
,code_profession INT(6)
,libelle_profession VARCHAR(1000)
)
;

-- Create Table population
DROP TABLE IF EXISTS population;
CREATE TABLE population(
code_insee INT(6)
,population_legale INT(7)
)
;

-- Create Table nuancier 
DROP TABLE IF EXISTS nuancier;
CREATE TABLE nuancier(
code VARCHAR(6)
,libelle VARCHAR(1000)
,ordre INT(3)
,definition VARCHAR(1000)
)
;

-- Create Table cities
DROP TABLE IF EXISTS villes;
CREATE TABLE villes(
id INT(6)
,departement_code INT(6)
,code_insee INT(6)
,zip_code INT(6)
,name VARCHAR(1000)
)
;
-- Create table categorie (Référentiel géographique )
DROP TABLE IF EXISTS categorie;
CREATE TABLE categorie(
code INT(6)
,nb_demplois INT(6)
,artisans_commerçants_chefs_dentreprise INT(6)
,cadres_et_profeffions_intellectuelles_superieures INT(6)
,professions_intermedaires INT(6)
,employes INT(6)
,ouvriers INT(6)
)
;

-- Create table departements
DROP TABLE IF EXISTS departements;
CREATE TABLE departements(
id INT(4)
,region_code INT(4)
,code INT(3)
,name VARCHAR(1000)
,nom_normalise VARCHAR(1000)
)
;


-- Ecrire la requête qui va créer un nouvelle utilisateur MySQL « RNE_user » avec pour mot de passe « RNE_password » et lui accorder tous les droits sur la base RNE. Utiliser cette utilisateur pour la suite.

-- Create RNE_user et attribution des privilèges
CREATE USER 'RNE_user'@'localhost' IDENTIFIED BY 'RNE_password';
-- Add all privileges to RNE_user
GRANT ALL PRIVILEGES ON * . * TO 'RNE_user'@'localhost';