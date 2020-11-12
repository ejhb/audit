#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:26:16 2020

@author: ludodata
"""
from random import randrange

class case:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        case = self.x, self.y
        listeCases.append(case)
    def adjacentes(jeu):
        caseAdjacentes = []
        caseAdjacentes.append(case.self.x +1, case.self.y +1)
        caseAdjacentes.append(case.self.x +1, case.self.y)
        caseAdjacentes.append(case.self.x +1, case.self.y -1)
        
    def __str__(self):
        return 'La case' + case + 'à été créee'

carte = [case(x,y) for l in longueur for L in largeur]


largeur = [i for i in range(1,(input("entrer la largeur")))]
couleurs = [i for i in range(1,input("entrer la longueur"))]

class creature:
    def __init__(self, nom, position):
        self.nom = nom
        self.position = position
        listeCreatures.append(nom)
    def choisirCible(jeu):
        for i in case.caseAdjacentes:
            if jeu.estOccupee(i):
                return case
            else:
                return randrange(case.caseAdjacentes)
    def __str__(self):
        return 'la creature ' + self.nom + ' à été créee et positionné à ' + str(self.position)
    
    
class jeu:
    def __init__(self, listeCases, listeCreature, tour, actif):
        self.listeCases = listeCases
        self.listeCreature = listeCreature
        self.tour = tour
        self.actif = actif
        tour = 0
    def estOccupee(case):
            if case != " ":
                return case

    def deplacer(creature, case):
        creature.choisirCible()
        if case == creature.position:
            print(creature.nom + "à gagner")
        else: jeu.tour += 1

listeCases = []
listeCreatures = []

crea1 = creature('Robert', '0,0')
crea2 = creature('Marcel', '3,3')
print(crea1)
print(crea2)



c0 = case(0,0)
c1 = case(0,1)
c2 = case(0,2)
c3 = case(0,3)
c10 = case(1,0)
c11 = case(1,1)
c12 = case(1,2)
c13 = case(1,3)
c20 = case(2,0)
c21 = case(2,1)
c22 = case(2,2)
c23 = case(2,3)
c30 = case(3,0)
c31 = case(3,1)
c32 = case(3,2)
c33 = case(3,3)

print(listeCases)
print(listeCreatures)