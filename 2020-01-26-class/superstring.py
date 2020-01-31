class superstring : 
  def __init__(self, chaine):
    self.ch = chaine
  def ajoute (self, char):
    self.ch += char
  def insert (self, char , i):
    self.ch = self.ch[:i] + char + self.ch[i:]
  def upper(self):
    self.ch = self.ch.upper()
  def capsdown(self):
    self.ch = self.ch.lower()
  def tri(self):         
    self.ch = self.ch.split()
    self.ch = "~".join(sorted(self.ch))
  def __str__(self):
    return "Type : Superstring " + "content : " + self.ch
    

s1 = superstring("ecoutez bien c'est important")

s1.tri()

print(s1)
  