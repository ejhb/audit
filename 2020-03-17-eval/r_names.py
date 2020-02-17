# 1

names_elus = "code (insee)	mode de scrutin	numliste	code (nuance de la liste)	numéro du candidat dans la liste	tour	nom	prénom	sexe	Date de naissance	code (profession)	libellé profession	nationalité"

def r_names(s):
    s2 = s.strip().replace('.','').replace(',','').replace(' ','_').replace('(','').replace(')','').replace("'",'').replace('é','e')
    print(s2)

r_names(names_elus)


# 2     











