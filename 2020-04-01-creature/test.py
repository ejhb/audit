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

def generate():
    xy = int(input("Veuillez entrer la largeur :\n"))
    yx = int(input("Veuillez entrer la longueur :\n"))
    largeur = [i for i in range(0,xy+1)]
    longueur = [i for i in range(0,yx)]
    plateau = []
    plateau = [case(l,L) for l in longueur for L in largeur]

    for i in plateau:
        print(i)
    return plateau







