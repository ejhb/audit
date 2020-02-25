import pandas as pd 


# • Lire le fichier « thanksgiving.csv » avec la librairie pandas et l’assigne à une variable data.
# • Spécifier dans les paramètre de la fonction permettant de lire le fichier
# « encoding=‘latin-1’ » car ce dataset n’est pas encodé normalement.
# • Utiliser le noms des colonnes contenu dans la 1 ère ligne du fichier.
# • Afficher les premières lignes du dataframe (une méthode enparticulier permet de le faire).

df = pd.read_csv('/home/joshua/Documents/git-workspace/audit/2020-02-25-analyse/thanksgiving.csv',encoding='latin-1')

df_limited = pd.read_csv('/home/joshua/Documents/git-workspace/audit/2020-02-25-analyse/thanksgiving.csv',encoding='latin-1',nrows=10)

print(df)

# • Afficher le noms des colonnes avec l’attribut columns.

df_2 = pd.read_csv('/home/joshua/Documents/git-workspace/audit/2020-02-25-analyse/thanksgiving.csv',encoding='latin-1',nrows=1000)

print(df_2.columns)

# • Utiliser la méthode Series.values_count() pour afficher le décompte du nombre de réponses pour chacune des modalités de la colonnes « Do you celebrate Thanksgiving? »

df_3 = pd.read_csv('/home/joshua/Documents/git-workspace/audit/2020-02-25-analyse/thanksgiving.csv',encoding='latin-1',nrows=1000)

do_data = df_3['Do you celebrate Thanksgiving?']

print(do_data.value_counts()) 


df_4 = pd.read_csv('/home/joshua/Documents/git-workspace/audit/2020-02-25-analyse/thanksgiving.csv',encoding='latin-1')

# • Filtrer et garder toute les ligne du dataframe pour lesquelles la réponse à la question « Do you celebrate Thanksgiving? » est « Yes ».
# • Assigner ce nouveau dataframe à data et affiché le.

is_yes = df[df['Do you celebrate Thanksgiving?'] == "Yes"]

print(is_yes)


# • Utiliser la méthode Series.values_count() pour afficher combien de fois chaque résultats apparait pour la question « What is typically the main dish at your Thanksgiving dinner? »

is_tofurkey = df[df['What is typically the main dish at your Thanksgiving dinner?'] == "Tofurkey"]

what_data = is_tofurkey['Do you typically have gravy?']

print(what_data)


