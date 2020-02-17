import re 

s = "code (insee) mode de scrutin numliste code (nuance de la liste) numéro du candidat dans la liste tour nom prénom sexe Date de naissance code (profession) libellé profession nationalité"

def r_names(s):
    s1 = []
    s2 = s.split()
    for i in s2 :
        i.replace(".","_").replace(",","_").replace(" ","_")
        s1.append(i)
    return s1

print(r_names(s))

def r_names():
    s1 = input('Entre la chaines à modif: ')
    s2 = s1.strip().lower().replace(' ', '_').replace(',','').replace('(','').replace(')','').replace("'",'').replace('é','e')
    print(s2)

r_names()






