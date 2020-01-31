from random import randrange

class Card : 
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return '('+str(self.value)+',' +str(self.suit)+')'


class Partie :
    def __init__(self, nbvalue, nbsuit, nbround):
        self.nbvalue = nbvalue
        self.nbsuit = nbsuit
        self.nbtour = nbround
    #partie starter doit regroupé le déroulement de la partie
    # def jouer
    def __str__(self):
        return '('+str(self.nbvalue)+','+str(self.nbsuit)+','+str(self.nbround)+')'   

# On initailise toutes les valeurs et couleurs que peuvent prendre les cartes 
valeurs = [i for i in range(1, 11)]
couleurs = [i for i in range(1,5)]

# on choisi le nombre de tour que va durée la partie et on initilise le score à 0

nbTours = 7
score = 0 

# Enfin on crée une liste de tuple pour représenter le paquet de cartes
paquet = [Card(c,v) for v in valeurs for c in couleurs]
main1, main2 = [], []

def pioche(paquet, nbTours):
    for i in range(nbTours):
        # Le joueur 1 tire une carte aléatoirement dans le paquet
        x = paquet[randrange(len(paquet))]
        # La carte est ajouté à la main du joueur 1 
        main1.append(x)
        # La carte est supprimé du paquet
        paquet.remove(x)
        # Idem pour le joueur 2 
        y = paquet[randrange(len(paquet))]
        main2.append(y)
        paquet.remove(y)
    return main1 , main2

main1, main2 = pioche(paquet, nbTours)
    
def plusGrandQue(x,y):
    return x.value > y.value or (x.value == y.value and x.suit > y.suit) 
    
 
for i in range(nbTours):
    if plusGrandQue(main1[i],main2[i]):
        score = 1
    else : 
        score = - 1

print("Vainqueur : " + ("joueur 1"if score > 0 else "joueur 2"))

