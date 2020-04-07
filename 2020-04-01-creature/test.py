# Principe du jeu :
# Des créature se déplace sur un damier, d’une case à la fois (Les diagonales sont autorisées). Si l’une d’elles arrive sur la case de l’autre, elle la capture et à gagné.
# Pour cela on va définir 3 classes :
# • Case, qui possède un attribut x et un attribut y.
# • Créature, qui possède un attribut nom, position.
# • Jeu, qui possède quatre attributs listesDesCases, listeDesCreatures, tour, et actif. 

# 1. Rédiger ces classe avec leurs constructeurs. Modifier leur méthode __str__ de façon à rendre leur affichage utile.

# Classe d'un case et des case adjacente 
class case:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# 3. Rédiger une méthode adjacentes(jeu) dans la classe Case, qui renvoie la liste des Case du jeu adjacentes à la case courante.        
    def adjacentes(jeu):
        caseAdjacentes = []
        caseAdjacentes.append(case.self.x +1, case.self.y +1)
        caseAdjacentes.append(case.self.x +1, case.self.y)
        caseAdjacentes.append(case.self.x +1, case.self.y -1)

    def __str__(self):
        return 'Case  ' + str(self.x) + ' de la largeur et ' + str(self.y) + ' de la longeur.'


class creature:
    def __init__(self, nom, position):
        self.nom = nom
        self.position = position
        listeCreatures.append(nom)
# 4. Rédiger une méthode choisirCible(jeu) dans la class Creature qui renvoie la case voisine occupée s’il en existe une, et une voisine aléatoire sinon.
# 7. Créez un programme où deux Creature s’affrontent en se déplaçant à l’aide de la méthode choisirCible(jeu) jusqu’à ce que l’une ait gagné.     
    def choisirCible(jeu):
        for i in case.caseAdjacentes:
            if jeu.estOccupee(i):
                return case
            else:
                return randrange(case.caseAdjacentes)
    def __str__(self):
        return 'la creature ' + self.nom + ' à été créee et positionné à ' + str(self.position)
    
    
class jeu:
    def __init__(self, plateau, listeCreature, tour, actif):
        self.plateau = plateau
        self.listeCreature = listeCreature
        self.tour = tour
        self.actif = actif
        tour = 0
# 2. Rédiger une methode estOccupee(case) dans la classe Jeu qui vérifie si la Case case est occupée.
    def estOccupee(case):
        if case != " ":
            return case
# 5. Rédiger une méthode deplacer(créature, case) dans la class Jeu qui, si c’est autorisé, déplace créature sur case, affiche le nom du vainqueur dans la console si la case case était occupée par une autre Creature, et sinon incrémente le tour et échange la Creature active (c’est désormais le tour de l’autre de se déplacer).
    def deplacer(creature, case):
        creature.choisirCible()
        if case == creature.position:
            print(creature.nom + "à gagner")
        else: jeu.tour += 1

# 6. Initialisé un plateau de taille 4x4 avec deux Creature positionnées dans les angles oposés.
# Fonction qui génère un plateau par les inputs de l'utilisateur.
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




