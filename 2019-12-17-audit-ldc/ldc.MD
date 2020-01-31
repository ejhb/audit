# <p align=center> VEILLE SUR LES DROITS D'ACCES </p>

## Les droits sur les SGBD :



### <p align=center> GRANT </p> 
**Confère des droits et des privilèges à un utilisateur, comme on pourrait donné des droit d'écriture et de lecture à un utilisateur ou bien sur un secteur (objet,table ect..).** 

Example :

```
GRANT privilege_ecrire
ON table_lepaysansurbain
TO {rafik |PUBLIC |role_superboss}
[WITH GRANT OPTION];
```

**Ici on donne le privilege 'ecrire' sur la table 'lepaysansurbain' à l'utilisateur 'rafik' avec le role 'superboss'.**

Source : <https://beginner-sql-tutorial.com/sql-grant-revoke-privileges-roles.html>

### <p align=center> REVOKE </p> 
**A exactement le même fonctionnement que GRANT, sauf qu'aulieu de conféré il retire des privilège.**

```
REVOKE privilege_ecrire
ON table_lepaysansurbain
TO {rafik |PUBLIC |role_superboss}
[WITH GRANT OPTION];
```

**Ici on retire le privilege "ecrire" sur la table 'lepaysansurbain' à l'utilisateur 'rafik' avec le role 'superboss'.** 


## LES TRANSACTION : 

**L'ors de l'implémentation au sain d'une SGBDR on peut faire face à deux problèmes : la fiabilité (une panne server) et l'accés concurrents DB c'est ce pourquoi une SGBDR nativement fonction sous un état transactionnel qui se déroule en 3 étape:**

1. **Le Début : qui est constitué de votre requête**
1. **Le Traitement : qui vous donne accés ou non à la lectre puis l'écriture**
1. **La Fin : qui définit votre requête de correcte ou incorrecte** 

<H3>ACID</H3>
        
1. **ATOMICITE : Ces 3 étapes sont fondamental à cet état transactionnel et aucune de ses étapes ne peut être bypass ce qui constitue la première des quatre propriété d'une transaction.** 
1. **COHERENCE : cohérence...**
1. **ISOLATION : les transaction n'ont aucunes interactions entre elles.**
1. **DURABILITE : La plupart du temps elle sont local est perdurent en cas de défaillance du server.**
            
Source: <https://stph.scenari-community.org/bdd/0/co/tra1_div.html>
        
## Les droits sur les élément d’une base de données :

### <p align=center> COMMIT </p>

**La commande COMMIT permet la validation ou non de la requête en fonction des conditions qui régissent la cohérence de la base de donnée.**


Example : 
```
DELETE from Customer where State = 'Texas';
COMMIT;
```

**Un de ses atouts principaux est de combler une potentielle panne la requête n' ou une incohérence.**

### <p align=center> ROLLBACK </p>

**On sait qu'une fois une transaction est terminé il n'y a pas moyen de l'annulé néanmoins on peut faire une nouvelle transaction enfin d'inverser un précédent COMMIT;**

Example : 
```
DELETE from Customer where State = 'Texas';
ROLLBACK;
```

Source: <https://www.journaldev.com/23932/sql-commit-sql-rollback>


### <p align=center> LOCK </p>



