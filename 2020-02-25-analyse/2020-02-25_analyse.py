import pandas as pd 


# Lire le fichier « thanksgiving.csv » avec la librairie pandas et l’assigne à une variable data.
# Spécifier dans les paramètre de la fonction permettant de lire le fichier
# « encoding=‘latin-1’ » car ce dataset n’est pas encodé normalement.
# Utiliser le noms des colonnes contenu dans la 1 ère ligne du fichier.
# Afficher les premières lignes du dataframe (une méthode enparticulier permet de le faire).

df = pd.read_csv('/home/joshua/Documents/git-workspace/audit/2020-02-25-analyse/thanksgiving.csv',encoding='latin-1')

df_limited = pd.read_csv('/home/joshua/Documents/git-workspace/audit/2020-02-25-analyse/thanksgiving.csv',encoding='latin-1',nrows=10)

print(df)

print(df_limited)

# Afficher le noms des colonnes avec l’attribut columns.

print(df.columns)

# Utiliser la méthode Series.values_count() pour afficher le décompte du nombre de réponses pour chacune des modalités de la colonnes « Do you celebrate Thanksgiving? »

do_data = df['Do you celebrate Thanksgiving?']

print(do_data.value_counts()) 

# Filtrer et garder toute les ligne du dataframe pour lesquelles la réponse à la question « Do you celebrate Thanksgiving? » est « Yes ».
# Assigner ce nouveau dataframe à data et affiché le.

is_yes = df[df['Do you celebrate Thanksgiving?'] == "Yes"]

print(is_yes)

# Utiliser la méthode Series.values_count() pour afficher combien de fois chaque résultats apparait pour la question « What is typically the main dish at your Thanksgiving dinner? »

is_tofurkey = df[df['What is typically the main dish at your Thanksgiving dinner?'] == "Tofurkey"]

what_data = is_tofurkey['Do you typically have gravy?']

print(what_data)

# Créer un objet Series indiquant avec des booléens les valeurs de la colonnes « Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. -Apple » qui sont nulles.Assigner le résultat à la variable « apple_isnull ».

apple_isnull = pd.isna(df['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple'])

print(apple_isnull)

# Créer un objet Series indiquant avec des booléens les valeurs de la colonnes « Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin » qui sont nulles.Assigner le résultat à la variable « pumpkin_isnull ».

pumpkin_isnull = pd.isna(df['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin'])

print(pumpkin_isnull)

# Créer un objet Series indiquant avec des booléens les valeurs de la colonnes « Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan » qui sont nulles.Assigner le résultat à la variable « pecan_isnull ».

pecan_isnull = pd.isna(df['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan'])

print(pecan_isnull)

# Combiner les trois objets Series avec l’operateur « & » et assigné le résultat à la variable « pies ».

pies = pecan_isnull & pumpkin_isnull & apple_isnull 

print(pies)

# Afficher les valeurs unique et combien de fois elle apparaissent dans la colonnes de pies.

print(pies.value_counts())

# Ecrire une fonction qui converti une chaîne de caractère en une valeurentière. Cela permettra de convertir les valeurs de la colonne « Age » enentiers. Cette fonction prendra en paramètre une chaîne de caractères (lesvaleurs actuelles de la colonne « Age »)
# Utiliser la fonction is_null() pour vérifier si les valeurs sont nulles. Ajouter unecondition if qui retourne None si la valeur est nulle.
# Séparer les chaine de caractère en fonction de l’espace (‘ ’) et extraire le 1 èreélément de la liste.
# Supprimer le caractère ‘+’ dans le résultat.
# Convertir le résultat en entier.
# Retourner le résultat.

def isnull(x):
    if pd.isnull(x):
        return None
    else : 
        l = x.split(' ')
        l = l[0]
        l = l.replace("+", "")
    return int(l) 
 

# Utiliser la méthode Series.apply() pour appliquer la fonction à chaque valeur de la colonne ‘Age’ du dataframe data. Assigner le résultat à la nouvelle colonne ‘int_age’ du dataframe.

df['int_age'] = df['Age'].apply(isnull)

print(df['int_age'])

# Appeler la méthode Series.describe() sur la colonne « int_age » du dataframe data et afficher le résultat.

print(df['int_age'].describe())

# Ecrire une fonction pour convertir les revenus en valeur unique de format entier.
# Utiliser la fonction isnull() pour vérifier si la valeur est nulle. Si c’est le cas, retourner « None ».
# Séparer la chaine de caractère en prenant l’espace comme délimiteur et extraire le premier élément de la liste résultante.
# Si le résultat vaut « Prefer » retourner « None ».
# Supprimer les caractères « $ » et « , ».
# Utiliser int() pour convertir le résultat en entier.
# Retourner le résultat.

def convert(x):
    if pd.isnull(x):
        return None
    else : 
        l = x.split(' ')
        l = l[0]
        if l == "Prefer":
            return None
        l = l.replace("$", "").replace(",", "")
    return int(l) 

# Utiliser la méthode Series.apply() pour appliquer la fonction précédente à chaquevaleur de la colonne « How much total combined money did all members of your HOUSEHOLD earn last year? » du dataframe data.
# Assigner le résultat à la nouvelle colonne « int_income » du dataframe data.

df['int_income'] = df['How much total combined money did all members of your HOUSEHOLD earn last year?'].apply(convert)
print(df['int_income'])


# Appeler la méthode Series.describe() à la colonne int_income du dataframe data et afficher le résultat.
print(df['int_income'].describe())

# Regarder de quel manière les personnages gagnant moins de 150 000 dollars voyagent.
# Filtrer data en sélectionnant seulement les valeur de « int_income » infèrieures à 150 000

inf_df = df['int_income'][df['int_income'] < 150000]
sup_df = df['int_income'][df['int_income'] > 150000]

df_inf = inf_df['How far will you travel for Thanksgiving?']
