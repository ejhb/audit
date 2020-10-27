# 7. Bash scripting: 
# 	* Télécharger toutes les ressources pdf présente dans l'url donnée à l'aide du logiciel `wget` et stocké dans un répertoire personnel. Executer plusieurs fois le script. Qu'observez vous ?
# 	* faire le même script python qui réalise la même tache, en se basant sur le script suivant: 

import urllib.request
with urllib.request.urlopen('http://www.perdu.com/') as f:
    html = f.read().decode('utf-8')

with open("my-file.html", "w") as f:
    f.write(html)

# Quand j'utilise le script dans le bash, ça recréé un nouveau ficher à chaque fois que j'entre la commande.
# Quand j'utilise python ça utilise toujour le même fichier et ça réécrit à l'intérieur. Je penses que la version python est plus rapide.