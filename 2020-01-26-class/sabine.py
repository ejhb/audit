from random import randrange

# on initialise toutes les valeurs et couleurs
# que peuvenet prendre les cartes

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    def __repr__(self):
        return '('+str(self.valeur)+',' +str(self.couleur)+')'

class Partie:
    def __init__(self, nbValeur, nbCouleur, nbTours):
        self.nbValeur = nbValeur
        self.nbCouleur = nbCouleur
        self.nbTours = nbTours
   # def jouer(self, main1, main2)
   #     return    
    
jeu = Partie(13, 4, 8)    

valeurs = [i for i in range(jeu.nbValeur +1) ]
couleurs = [i for i in range(jeu.nbCouleur +1)]
nbTours = jeu.nbTours
# on choisit le nombre de tour que va durer la partie 
# et on initialise le score à 0

nbTours = 7
score = 0

# Enfin on crée une liste de tuple 
# pour représenter le paquet de cartes


paquet = [ Carte(v, c) for v in valeurs for c in couleurs]
main1, main2 = [], []

def pioche(paquet, nbTours):
    for i in range (nbTours):
    # Le joueur 1 tire une carte aléatoirement dans le paquet            
        x = paquet[randrange(len(paquet))]
    # La carte est ajoutée à la main du joueur 1
        main1.append(x)
    # La carte est supprimée du paquet
        paquet.remove(x)
    # idem pour le joueur 2
        y = paquet[randrange(len(paquet))]
        main2.append(y)
        paquet.remove(y)
    return main1, main2    

main1, main2 = pioche(paquet, nbTours)

# original code

#for i in range (nbTours):
#    # Le joueur 1 tire une carte aléatoirement dans le paquet
#    x = paquet[randrange(len(paquet))]
#    # La carte est ajoutée à la main du joueur 1
#    main1.append(x)
#    # La carte est supprimée du paquet
#    paquet.remove(x)
#    # idem pour le joueur 2
#    y = paquet[randrange(len(paquet))]
#    main2.append(y)
#    paquet.remove(y)

# To be used in the case of unpacking tuples

# def plusGrandQue(x,y,w,z):
#    s = 0    
#    if x > w or (x == w and y > z):
#        s += 1
#    else:
#        s -=1
#    return s == 1   

def plusGrandQue(x,y):  
    return x[0]> y[0] or (x[0] == y[0] and x[1] > y[1])
    return x.valeur > y.valeur or (x.valeur == y.valeur and x.couleur > y.couleur)  
    
for i in range(nbTours):
    if plusGrandQue(main1[i], main2[i]):
        score = 1
    else:
        score = -1
    #score = plusGrandQue(*main1[i],*main2[i]) 
    
#    if main1[i][0] > main2[i][0] or ( 
#            main1[i][0] == main2[i][0] and main1[i][1]> main2[i][1]):
#        score += 1
#    else :
#        score -= 1

print(" Vainqueur : " + ("joueur 1" if score > 0 else "joueur2"))        