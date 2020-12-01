import numpy as np



app = 'Anthony Constant Joshua Fatima Julien Bassem Caroline Dan Ines Nidhal Sacia Xavier Roger Hachem Jean-Pierre Myriam Ludo Olivier Pierre-Etienne Wiem Cecilia'.split()
s = app
 
np.random.seed(1)
rapp = [s[i] for i in np.random.choice(21, 21, replace=False)]
for i in range(4):
    e = rapp
    print(e[4*i:4*i+4] + ([e[-1]] if i == 3 else []))