# 1. Créer une class data qui hérite du formulaire et possède un attribut supplémentaire id. Une méthode doit permettre d’initialiser cette identifiant comme une combinaison de caractères pris dans chaque autre attribut.

class formulaire:
    def __init__(self, nom, prenom, naissance):
        self.nom = str(nom)
        self.prenom = str(prenom)
        self.naissance = naissance
    def _set_naissance(self, naissance):
        if str(type(naissance)) == "<class 'list'>":
            naissance = ''.join(naissance)
        if str(type(naissance)) == "<class 'str'>" and naissance.isnumeric():
            naissance = int(naissance)
        if str(type(naissance)) == "<class 'int'>":
            self._naissance = naissance
        #else:
        #    self._naissance = 1900
    def _get_naissance(self):        
        print("Année de naissance :" , self._naissance)
        return   self._naissance 
    naissance = property(_get_naissance, _set_naissance)
    
    def _set_nom(self, nom):
        if str(type(nom)) == "<class 'str'>":
            nom = str(nom)
            self._nom = nom
    
    def _get_nom(self):
        return   self._nom
    nom = property(_get_nom, _set_nom)
    
    def _set_prenom(self, prenom):
        if str(type(prenom)) == "<class 'str'>":
            prenom = str(prenom)
            self._prenom = prenom
    def _get_prenom(self):
        return   self._prenom
    prenom = property(_get_prenom, _set_prenom)
    
    def age(self):
        return 2020 - self._naissance
    
    def majeur(self):
        return self.age() >= 18
    
    def memeFamille(self, formulaire):
        return self.nom == formulaire.nom

class data(formulaire) :
    
    def __init__(self, nom, prenom, naissance) :
        formulaire.__init__(self, nom, prenom, naissance)
    
    def build_id(self, id) :
        self.id = self.nom[:2] + self.prenom[:2] + str(self.age())

jd = data('Doe', 'John', 1999)
ad = data('Doe', 'Jueeph', 2001) 
jd.build_id()
ad.build_id()
print(jd.id)
print(ad.id)


