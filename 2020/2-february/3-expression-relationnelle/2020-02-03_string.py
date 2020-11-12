from re import findall

# Ecrire une fonction hascap(s) qui renvoie tout les mots de la chaînes commençant par une majuscule. Pour ce faire utiliser la fonction ord() pour obtenir le code ASCII des lettres (Les lettres majuscule ont un code allant de 65 à 90).

def hascaps(x):
    l1= []
    l2 = x.split()
    for i in l2:
        if ord(i[0]) in range(65,91):
            l1.append(i)
    return print(l1)


# Proposer une fonction inflation(s) qui va doubler la valeur de tout les nombre dans la chaine s. Exemple : « Le prix est de 27 euros » devient « Le prix est de 54 euros ». Utiliser la fonction enumerate() pour lancer une boucle for (Taper dans Google « enumerate boucle for ».)

# def inflation(x):
#     l = x.split()
#     for num in l : 
#         if num.isnumeric():
#             v = int(num)
#             op = v**2
#     print(l)

# x = "Le prix est de 27 euros"

def inflation(s):
    enum = enumerate(s.split())
    for i in enum:
        if i[1].isnumeric():
            s2 = s.replace(i[1],str(int(i[1])*2))            
    return s2

# print(inflation(x))

# 3. Proposer une fonction lignes qui à partir d’une long chaîne s (>100 caractères) renvoie une liste de chaîne de caractères contenant chacun 24 caractères maximum et terminant par un espace. Voici un exemple de chaîne sur le quel vous pouvez travailler :

# s = "Onze ans déjà que cela passe vite Vous "
# s += "vous étiez servis simplement de vos armes la "
# s += "mort n‘éblouit pas les yeux des partisans Vous «
# s += "aviez vos portraits sur les murs de nos villes«


# Algorithme :
    # Entrée : Longue chaîne de caractère
    # • Traitement :
        # • Partage de la chaîne de caractère en une liste de mots
        # • On crée une liste vide lignes
        # • Pour tout mot dans la liste :
        # • On ajoute un espace à mot
        # • Si la longueur du dernier élément de la liste vide + la longueur du mot < 24 :
        # • On ajoute le mot au dernier élément de la liste ligne (+= mot)
        # • Si non :
        # • On ajoute le mot en tant que dernier élément de la liste
    # • Sortie : liste ligne



# x = "Je suis avec mes bro Je suis avec mes bro Je suis avec mes bro Je suis avec mes bro Je suis avec mes bro Je suis avec mes bro Je suis avec mes bro"

def ligne(x):
    s1 = x.split()
    s2 = [""]
    for i in s1 : 
        i += " "
        if len(s2[-1]) + len(i) <= 24:
            s2[-1] += i
        else : 
            s2.append(i[-1])
    print(s2)




# 4. Proposer un programme qui renvoie la liste de tout les nombres (ycompris décimaux et négatifs) d’une chaîne de caractères. A tester sur la chaîne : « Les 2 maquereaux valent 6.50 euros ».

def return_num(x):
    indice =  '[-]*[0-9][\. or \,]?[0-9]*'
    return (findall(indice,x))

x = "Les 2 maquereaux valent 6.50 euros"
print(return_num(x))


# 5. Proposer une fonction arrondi(s) qui dans la chaîne s troncature tout les nombre décimaux. On autorise les nombres négatifs.Pour ce faire, vous avez la possibilité d’utiliser : des () pour désigner des blocs de données dans l’expression rationnelle. pour remplacer chacun des blocs l’expression est r’\1_\2_’.

