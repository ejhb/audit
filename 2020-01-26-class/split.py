class formulaire: 
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

jd = formulaire('Doe', 'John',2005)
ad = formulaire ('doe','Alice',2000)

print(jd.majeur())
print(ad.majeur())
print(jd.memeFamille(ad))