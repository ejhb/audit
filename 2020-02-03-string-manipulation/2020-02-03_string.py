# Ecrire une fonction hascap(s) qui renvoie tout les mots de la chaînes commençant par une majuscule. Pour ce faire utiliser la fonction ord() pour obtenir le code ASCII des lettres (Les lettres majuscule ont un code allant de 65 à 90).



# Proposer une fonction inflation(s) qui va doubler la valeur de tout les nombre dans la chaine s. Exemple : « Le prix est de 27 euros » devient « Le prix est de 54 euros ». Utiliser la fonction enumerate() pour lancer une boucle for (Taper dans Google « enumerate boucle for ».)



s = "Le prix est de 27 euros"
l = s.split()
x = 1
for num in l : 
    if num.isnumeric():
        num = num**2
print(s)
print(num)


