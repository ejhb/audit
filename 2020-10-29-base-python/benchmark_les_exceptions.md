Qu'est-ce qu'une exception ? 

Dès l'ors que l'on commence à codé et donné des instructions à l'interpréteur ont peut s'attendre à faire des erreur qui seront mis en evidence par l'ide ou la console. Ces erreur sont appeler des exceptions.
Le débugage étant une majeur partie de notre travaille de déveulopper il est indispensable de le comprendre à fin de les résoudre rapidement.

Quand on rencontre une erreur avec python, il lève une exception. 

```
# Exemple classique : test d'une division par zéro
variable = 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: int division or modulo by zero
```

Attardons-nous sur la dernière ligne. Nous y trouvons deux informations :

    - ZeroDivisionError: le type de l'exception ;
    - int division or modulo by zero : le message qu'envoie Python pour vous aider à comprendre l'erreur qui vient de se produire.

On trouve différents types d'exceptions que Python va utiliser en fonction de la situation. Le type d'exceptionValueError, notamment, pourra être levé par Python face à diverses erreurs de « valeurs ». 

Introduction au bloc d'instruction try

On va parler ici de bloctry. Nous allons en effet mettre les instructions que nous souhaitons tester dans un premier bloc et les instructions à exécuter en cas d'erreur dans un autre bloc. Sans plus attendre, voici la syntaxe :

```
annee = input()
try: # On essaye de convertir l'année en entier
    annee = int(annee)
except:
    print("Erreur lors de la conversion de l'année.")
```

Le mot-clé "try" suivi des deux points « : » (try signifie « essayer » en anglais).

Le bloc d'instructions à essayer. "annee = int(annee)

Le mot-clé "except"  suivi, une fois encore, des deux points « : ».(expect qui signifie dans ce contect « ce que l'ont peut attendre » ) Il se trouve au même niveau d'indentation que letry.

Le bloc d'instructions qui sera exécuté si une erreur est trouvée dans le premier bloc."print("Erreur lors de la conversion de l'année.")

Forme bloc d'instruction try plus complète

try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")

De la même manière que python nous renvoi le type de l'erreur en question. On peut attribué à chaque type d'erreur auxquelle s'attendre de nouvelles instructions.

NameError: l'une des variables numerateur ou denominateur n'a pas été définie (elle n'existe pas). 

TypeError: l'une des variables numerateur ou denominateur ne peut diviser ou être divisée (les chaînes de caractères ne peuvent être divisées, ni diviser d'autres types, par exemple). 

ZeroDivisionError: encore elle ! Sidenominateurvaut 0, cette exception sera levée.

