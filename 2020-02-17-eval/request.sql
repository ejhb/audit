-- 8. Quel sont les parties politiques qui dans leur libellé comporte le terme « Union »
-- 9. Quels élus du département du « var » sont nais entre le mois de juin et aout ?
-- 10. Quel est l’âge moyen des élus homme au 01/01/2014 ? Celui des élus femme ?
-- 11. Afficher la population totale du département des « Bouches-du-Rhône »
-- 12. Quel sont les 10 départements comptant le plus d’ouvriers.
-- 13. Afficher le nombre d’élus regrouper par nuance politique et par département.
-- 14. Afficher le nombre d’élus regroupé par nuance politique et par villes pour le département des « Bouches-du-Rhône ».
-- 15. Afficher les 10 départements dans lesquelles il y a le plus d’élus femme, ainsi que le nombre d’élus femme correspondant.
-- 16. Donner l’âge moyen des élus par départements au 01/01/2014. Les afficher par ordre décroissant.
-- 17. Afficher les départements où l’âge moyen des élus est strictement inférieur à 54 ans.

USE RNE;

-- 8. Quel sont les parties politiques qui dans leur libellé comporte le terme « Union »

SELECT *
FROM nuancier
WHERE libelle LIKE '%Union%';

-- 9. Quels élus du département du « var » sont nais entre le mois de juin et aout ?

SELECT nom
,prenom
,v.name
FROM elus e
INNER JOIN villes v ON e.code_insee = v.code_insee
INNER JOIN departements d ON v.departement_code = d.code
WHERE d.name = "Var" 
AND MONTH(date_de_naissance) 
BETWEEN "06" AND "08"; 

-- 10. Quel est l’âge moyen des élus homme au 01/01/2014 ? Celui des élus femme ?
DROP TABLE IF EXISTS age_calcule;

CREATE TABLE age_calcule AS

SELECT nom
,prenom
,sexe
,TIMESTAMPDIFF(year,date_de_naissance,"2014-01-01") AS age
FROM elus
;

SELECT AVG(age)
,sexe
FROM age_calcule
GROUP BY sexe
;

-- 11. Afficher la population totale du département des « Bouches-du-Rhône »

SELECT SUM(population_legale) as total_pop
,departements.name as dep_name
FROM population
INNER JOIN villes v
ON population.code_insee = v.code_insee
INNER JOIN departements 
ON v.departement_code = departements.code 
WHERE departements.name = "Bouches-du-Rhône"
;


-- 12. Quel sont les 10 départements comptant le plus d’ouvriers.

SELECT COUNT(ouvriers) as count_ouv -- SUM INSTEAD OF COUNT
,d.name
FROM categorie c 
INNER JOIN population p
ON c.code = p.code_insee
INNER JOIN villes v 
ON p.code_insee = v.code_insee
INNER JOIN departements d 
ON v.departement_code = d.code
GROUP BY d.name 
ORDER BY count_ouv DESC
LIMIT 10
;

-- 13. Afficher le nombre d’élus regrouper par nuance politique et par département.

SELECT COUNT(nom) AS 
nb_elu 
,libelle AS parti_pol 
,departement_code AS num_departement
FROM elus e
INNER JOIN nuancier n
ON e.code_nuance_de_la_liste = n.code
INNER JOIN villes v
ON e.code_insee = v.code_insee
GROUP BY libelle, departement_code
;

-- 14. Afficher le nombre d’élus regroupé par nuance politique et par villes pour le département des « Bouches-du-Rhône ».

SELECT COUNT(nom) AS 
nb_elu 
,libelle AS parti_pol 
,departement_code AS num_departement
FROM elus e
INNER JOIN nuancier n
ON e.code_nuance_de_la_liste = n.code
INNER JOIN villes v
ON e.code_insee = v.code_insee
GROUP BY libelle, departement_code
HAVING departement_code = "13"
;


-- 15. Afficher les 10 départements dans lesquelles il y a le plus d’élus femme, ainsi que le nombre d’élus femme correspondant.

SELECT COUNT(nom) AS nb_elu_femme
,d.name
FROM elus e
INNER JOIN villes v 
ON v.code_insee = e.code_insee
INNER JOIN departements d
ON v.departement_code = d.code
;

-- 16. Donner l’âge moyen des élus par départements au 01/01/2014. Les afficher par ordre décroissant.

DROP TABLE IF EXISTS age_calcule_dep;

CREATE TABLE age_calcule_dep AS

SELECT nom
,prenom
,sexe
,TIMESTAMPDIFF(year,date_de_naissance,"2014-01-01") AS age
,v.departement_code as code_dep
FROM elus e
INNER JOIN villes v
ON e.code_insee = v.code_insee
;

SELECT AVG(age) as avg_age
,code_dep as dep
FROM age_calcule_dep
GROUP BY code_dep ASC
;
-- 17. Afficher les départements où l’âge moyen des élus est strictement inférieur à 54 ans.

DROP TABLE IF EXISTS age_calcule_age_inf_dep;

CREATE TABLE age_calcule_age_inf_dep AS

SELECT nom
,prenom
,sexe
,TIMESTAMPDIFF(year,date_de_naissance,"2014-01-01") AS age
,v.departement_code as code_dep
FROM elus e
INNER JOIN villes v
ON e.code_insee = v.code_insee
;

SELECT AVG(age) as avg_age
,code_dep as dep
FROM age_calcule_age_inf_dep
GROUP BY dep 
HAVING avg_age < 54
;

