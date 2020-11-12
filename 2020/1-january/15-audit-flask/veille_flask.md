# <p align=center>FLASK</p>

## <p align=center>C'est quoi ?</p>


**Flask est un micro-framework régie par python, sa légèreté et sa versatilité permet de concevoir des application web rapide et efficace. C'est une manière de déployer un server web redoutable du à sa très grandes varités d'outils et sa facilité à être développer.**

**Une de ses plus grandes force est de lui intégré différentes librairie/extension comme l'user management qui comprend : de la création d'un login à son changement de mot de passe ect.. Comparé à Django ou d'autre framework du même style il est plus flexible et est moins rules-restricted.**

## <p align=center>Environement</p>

**Pour commencer à travailler sur un projet avec Flask il est très suggérer de mettre ne place une environement virtuel. C'est un bonne moyen d'évité d'éventuel conflits à travers des projects notament vis à vis de l'importation de librairie.**

## <p align=center>Setup venv</p>

**Pour installer virtualenv use: ```$ pip3 install virtualenv```. Ensuite déplacer vous dans le dossier de votre projet puis use: ```$ virtualenv venv``` ceci va créé un dossier nommé venv dans lequel sera regroupé tout nos exécutable requis pour commencé à travaillé dans un environement séparé.**

***Hint : .gitignore ce folder pour votre github.***

**Tout au long de la veille nous allons utiliser Python 3. Vous pouvez à tout moment changer la version de l'interpreter avec la command: ```$ virtualenv -p /usr/bin/python3.6 venv```**

**L'activation votre environement virtuel à chaque fois que vous serez amenez à travaillé dans votre projet (si toute fois vous décidez d'utiliser un venv)```$ source venv/bin/activate``` et ```$ deactivate```**
Lorem ipsum dolor sit amet, consect adipis elit minim veniam ettis inkeras.re en place donc autant prendre de bonne habitude de travail.**

## Script

```
from flask import Flask
app = Flask(__name__)
​
@app.route(‘/’)
def hello_world():
   return ‘Hello, World!’
```

**Enregirstrons ce bout de script dans un fichier "name.py".** 

**Si on décide d'exécuter notre application on run le script avec python. Une fois dans le dossier ```$ python3 "name.py"```**.

**L'output suivant devrait être déclaré:**

```
 * Serving Flask app "name.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
**Votre server est donc établis en local est disponible dans une navigateur web à l'addresse indiqué:** http://127.0.0.1:5000/ . 

**En s'y rendant on peut remarquer une page web avec un "Hello, World!".**

**Revenons à notre script pour le décrypter brièvement:** 

```
1. from flask import Flask
2. app = Flask(__name__)
​3. 
4. @app.route(‘/’)
5. def hello_world():
6.   return ‘Hello, World!’
```

- Ligne 1 nous importons flask.
- Ligne 2 ont créé une instance de class pour Flask, c'est une variable spécial qui a pour valeur string:"__ main__".
- Ligne 4 '/' détermine un chemin, ici nous somme dans le home page où sera displayed la fonction sur la ligne qui suit. On aurait pu definir un autre chemin d'accés par example: '/login' pour y accéder http://127.0.0.1:5000/login . C'est la fonction route de la librairie app. 
- Ligne 5 on définit notre function hello_world().
- Ligne 6 cette function retourne 'Hello, World!'.

SOURCE : https://pythonhow.com/how-a-flask-app-works/ & https://dev.to/gajesh/the-complete-flask-beginner-tutorial-124i

