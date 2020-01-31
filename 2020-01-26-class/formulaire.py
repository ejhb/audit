class Formulaire : 
    def __init__(self, nom, prenom, anneeNaissance):
        self.nom = nom.upper()
        self.prenom = prenom.upper()
        self.anneeNaissance = anneeNaissance 
    def age(self):
        return 2020 - self.anneeNaissance
    def majeur(self):
        return self.age() >= 18
    def memeFamille(self, formulaire):
        return self.nom == formulaire.nom
    def checkAlias(self, checked):
        return self.nom == checked.nom and self.prenom == checked.nom and self.anneeNaissance == checked.anneeNaissance
    def __str__(self):
        return (self.nom +"," + self.prenom +","+ str(self.anneeNaissance))
      
def extract(x,y):
    x.append(y)

my_list = []

jd = Formulaire('Doe', 'John',2005)

extract(my_list,jd)


ad = Formulaire('Doe','Alice',2000)
extract(my_list,ad)

za = Formulaire('Doe','Sophie',1999)
extract(my_list,za)

az = Formulaire('Doe','Xavier',1997)
extract(my_list,az)

a = sorted(my_list, key=lambda year: year.anneeNaissance)
for i in a : 
    print(i)