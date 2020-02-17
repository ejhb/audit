# 1 Ecrire une fonction python r_names() qui admet pour entrer une de ces chaînes de
# caractères et qui retourne une liste de nom de colonnes.
# Les espaces, les « ‘ » et les « . » doivent être remplacé par des « _ ».
# Les « é » et « è » doivent être remplacé par des « e ».
# Les « , », « ) » et « ( » doivent être supprimées.

lib_elus = "code (insee)	mode de scrutin	numliste	code (nuance de la liste)	numéro du candidat dans la liste	tour	nom	prénom	sexe	Date de naissance	code (profession)	libellé profession	nationalité"

lib_nuancier = "code	libellé	ordre	définition_"

lib_cities = "id	departement_code	code_insee	zip_code	name"

lib_categorie = "Code	Nb d'emplois	Artisans, commerçants, chefs d'entreprise	Cadres et professions intellectuelles supérieures	Professions intermédaires	Employés	Ouvriers"

lib_population = "Code insée	Population légale"

lib_departements = "id	region_code	code	name	nom normalisé"

def r_names(s):
    s2 = s.lower().replace('.','').replace(',','').replace(' ','_').replace('(','').replace(')','').replace("'",'').replace('é','e')
    print(s2)

# r_names(lib_elus)
# r_names(lib_nuancier)
# r_names(lib_cities)
# r_names(lib_categorie)
# r_names(lib_population)
# r_names(lib_departements)

# 2  Ecrire une fonction python parse_dates() qui admet pour entrer la liste renvoyer par r_names() et qui retourne une liste contenant seulement les noms    de colonnes commençant par « Date». 

  











