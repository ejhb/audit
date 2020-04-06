class case:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def adjacentes(jeu):
        caseAdjacentes = []
        caseAdjacentes.append(case.self.x +1, case.self.y +1)
        caseAdjacentes.append(case.self.x +1, case.self.y)
        caseAdjacentes.append(case.self.x +1, case.self.y -1)
        
    def __str__(self):
        return 'La case positionné en ' + str(self.x) + ' de la largeur et ' + str(self.y) + ' de la longeur.'

xy = int(input("Veuillez entrer largeur :\n"))
yx = int(input("Veuillez entrer longueur :\n"))

largeur = [i for i in range(1,xy)]
longueur = [i for i in range(1,yx)]

carte = [case(l,L) for l in longueur for L in largeur]

for i in carte:
    print(i)



