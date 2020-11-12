#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:09:39 2020

@author: utilisateur
"""

# LISTE LIBELLE : 
lib_elus = "code (insee)	mode de scrutin	numliste	code (nuance de la liste)	numéro du candidat dans la liste	tour	nom	prénom	sexe	Date de naissance	code (profession)	libellé profession	nationalité"

lib_nuancier = "code	libellé	ordre	définition_"

lib_cities = "id	departement_code	code_insee	zip_code	name"

lib_categorie = "Code	Nb d'emplois	Artisans, commerçants, chefs d'entreprise	Cadres et professions intellectuelles supérieures	Professions intermédaires	Employés	Ouvriers"

lib_population = "Code insée	Population légale"

lib_departements = "id	region_code	code	name	nom normalisé"

# FONCTION NORMALISATION NOM
def r_names(s):
    s2 = s.lower().replace('.','').replace(',','').replace(' ','_').replace('(','').replace(')','').replace("'",'').replace('é','e')
    s1 = s2.split()
    return(s1)

import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://RNE_user:RNE_password@localhost/RNE')

# FONCTION IMPORTATION XLXS 
def chargement(fichier_xls, table_sql,rows_to_skip , s):
    x = r_names(s)
    df = pd.read_excel(fichier_xls, delimiter='|',skiprows=rows_to_skip, names = x )
    
    df.to_sql(table_sql, con=engine, if_exists='append', index=False)
    
    return print('tableau', table_sql, 'has been filled')

categorie = '/home/joshua/Documents/git-workspace/audit/2020-03-17-eval/raw_doc/categorie_professionelle.xlsx'

villes = '/home/joshua/Documents/git-workspace/audit/2020-03-17-eval/raw_doc/cities.xlsx'

nuancier = '/home/joshua/Documents/git-workspace/audit/2020-03-17-eval/raw_doc/codes_nuances.xlsx'

departements = '/home/joshua/Documents/git-workspace/audit/2020-03-17-eval/raw_doc/departments.xlsx'

elus = '/home/joshua/Documents/git-workspace/audit/2020-03-17-eval/raw_doc/elus_mun2014.xlsx'

population = '/home/joshua/Documents/git-workspace/audit/2020-03-17-eval/raw_doc/population2017.xlsx'

chargement(categorie, 'categorie',1, lib_categorie)
chargement(nuancier, 'nuancier', 1, lib_nuancier)
chargement(villes, 'villes', 1, lib_cities)
chargement(departements, 'departements', 1, lib_departements)
chargement(population, 'population', 1,lib_population)
chargement(elus, 'elus', 1 , lib_elus)