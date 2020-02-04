#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:11:49 2020

@author: utilisateur
"""

from random import randrange

# On définit la classe Carte qui associe une valeur et une couleur à chaque carte
# on définit ainsi l'affichage en forme de tuple (valeur, couleur)
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    def __repr__(self):
        return '('+str(self.valeur)+',' +str(self.couleur)+')'

# On définit la classe Partie qui va décrir le déroulement d'une partie       
class Partie:
# D'abord on initialise le nombre de valeurs et de couleurs que pourront avoir nos cartes
#  et le nombre de tours par jeu
    def __init__(self, nbValeur, nbCouleur, nbTours):
        self.nbValeur = nbValeur
        self.nbCouleur = nbCouleur
        self.nbTours = nbTours
    def jouer(self):
# Ensuite dans la méthode jouer nous allons définir les mains en faisant appel à la fonction pioche
        self.main1, self.main2 = pioche(paquet,nbTours)
# Puis on compare les cartes piochés par les deux joueurs selon leur valeur d'abord et leur couleur après
        self.score = 0
        for i in range(self.nbTours):
            if plusGrandQue(self.main1[i], self.main2[i]):
                self.score = 1
            else:
                self.score = -1
# Finalement on définit l'affichage de cette méthode selon l'identité du vaiqueur jeu
        print(" Vainqueur : " + ("joueur 1" if self.score > 0 else "joueur2"))    
# Option to define repr in the method, then print(obj) needs to be called 
#    def __repr__(self):
#        return " Vainqueur : joueur 1" if self.score > 0  else "Vaiqueur :joueur2"


def pioche(deck, nbPlay):
    hand1, hand2 = [], []
    for i in range (nbPlay):
    # Le joueur 1 tire une carte aléatoirement dans le paquet            
        x = deck[randrange(len(deck))]
    # La carte est ajoutée à la main du joueur 1
        hand1.append(x)
    # La carte est supprimée du paquet
        paquet.remove(x)
    # idem pour le joueur 2
        y = deck[randrange(len(deck))]
        hand2.append(y)
        paquet.remove(y)
    return hand1, hand2    

# la fonction plusGrandque sert à évaluer les mains des joueur pour déterminer le vainqueur
# en comparant les valeurs les cartes des deux joueurs ou sinon, la couleur qui emporte
def plusGrandQue(x,y):  
   # return x[0]> y[0] or (x[0] == y[0] and x[1] > y[1])
    return x.valeur > y.valeur or (x.valeur == y.valeur and x.couleur > y.couleur)

        
jeu = Partie(13, 4, 9)    

valeurs = [i for i in range(1,jeu.nbValeur +1) ]
couleurs = [i for i in range(1,jeu.nbCouleur +1)]
nbTours = jeu.nbTours
paquet = [ Carte(v, c) for v in valeurs for c in couleurs]

jeu.jouer()
# in case repr is used :
#print(jeu)



#score = 0
#

#
#main1, main2 = [], []
#main1, main2 = jeu.jouer()
#
#for i in range(jeu.nbTours):
#    if plusGrandQue(main1[i], main2[i]):
#        score = 1
#    else:
#        score = -1
#
#print(" Vainqueur : " + ("joueur 1" if score > 0 else "joueur2"))        
#        
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

  
    

    #score = plusGrandQue(*main1[i],*main2[i]) 
    
#    if main1[i][0] > main2[i][0] or ( 
#            main1[i][0] == main2[i][0] and main1[i][1]> main2[i][1]):
#        score += 1
#    else :
#        score -= 1



    
    
    
    
    
    
    