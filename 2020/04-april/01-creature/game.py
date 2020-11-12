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
        case = self.x + self.y
        listeCases = []
        listeCases.append(case)
    def adjacentes(jeu):
        caseAdjacentes(self.x +1, self.y +1)
        caseAdjacentes(self.x +1, self.y)
        caseAdjacentes(self.x +1, self.y -1)


        
    def __str__(self):
        return 'La case' + case + 'à été créee'
    
# class creature:
#     def __init__(self, nom, position):
#         self.nom = nom
#         self.position = position
#         listeCreature = []
#         listeCreature = nom.append + position.append
#     def choisirCible(jeu):
#         for i in caseAdjacentes:
#             if i estOccupee(i):
#                 return case
#             else:
#                 return randrange(caseAdjacentes)
#     def __str__(self):
#         return 'la creature' + self.nom + 'à été créee et positionné à' + self.position
    
    
# class jeu:
#     def __init__(self, listeCases, listeCreature, tour, actif):
#         self.listeCases = listeCases
#         self.listeCreature = listeCreature
#         self.tour = tour
#         self.actif = actif
#         tour = 0
#     def estOccupee(case):
#             if case != " ":
#                 return case

#     def deplacer(creature, case):
#         choisirCible()
#         if case = position:
#             print(self.nom + "à gagner")
#             break
#         else: tour += 1

longueur = 2 
largeur = 2
carte = case(longueur,largeur)

print(carte)
print(largeur)