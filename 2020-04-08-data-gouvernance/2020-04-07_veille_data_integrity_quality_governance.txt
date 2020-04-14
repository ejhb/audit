                                                                GOUVERNANCE DE LA DONNE

## Qu'est-ce que le data gouvernance : DIAPO 2:

La gouvernance de la donnée est un modèle de cycle de vie de la donnée qui va décidé des étape à franchir par la donnée de sa collecte à sa retitution dans un data center ou bien un data lake. Avant même de collecté de la donnée on va s'intéroger de comment on va le faire, avec quel outils et dans quel but. Géneralement au sein d'une même entreprise un seul modèle va être instauré de sorte à uniformisé l'output de ses application qui à un moment ou un autre vont se retrouver dans un data center. 

Au sein d'une entreprise il peut y avoir une entité destiné à la gouvernance de la donnée mais ce n'est pas toujours le cas. Donc sur quel axe pouvons nous nous appuyer pour savoir si cela est nécessaire.

## Que prendre en compte DIAPO 3:

- Premièrement la taille de l'entrepise
- Deuxièmement temps ou l'argent
- Et enfin à qui est déstiné l'application ? Serat-elle public ou bien privé/interne ?

## Alternative DIAPO 4 :

Avant même de mettre en place un MDM ( Master data management ),la gouvernance de la donnée c'est avant tout beaucoup de bon sens et donc un consencius dès la collecte, par éxemple: quel format monétaire allons nous choisir: des euros ou bien des livres, le séparateur une virgule ou bien un point, un format de date internationnal donc les mois avant les jours ou encore certain caractères spéciaux et accents. Ca commence donc par de petit geste au cours d'une eventuel formation que l'on commence à instauré une gouvernance.

## Les Avantages DIAPO 5 : 

Un modèle de gouvernance bien designé en fonction des besoin, evite d'alloué plus d'argent et de temps a de service de maintenance comme le data cleaning et améliore donc la fluidité du cycle de vie ainsi que sa compréhension. 

## La qualité et/ou l’intégrité d’une donnée DIAPO 6 :  

Le therme de data quality, fait référence à sa qualité ainsi qu'a son intégritée on se base sur quel critère ? La bonne qualité d'une donnée c'est pas une donnée qui n'a pas d'accent, c'est pas une donnée en capital case, c'est tout simplement une donnée qui respecte les points de contrôle établis par une modèle de gouvernance. 

Ces données vont être utilisé dans des algorithme procédural charger à prendre des déçisions il est donc essentiel que ses données soit pertinente. Le plus anodine des donnée est sensible et ce pour n'importe quel opérateur data. Notamment en milieu hospitalier où il est fondamental d'avoir des données pertinente comme pour un dossier qui va être attribué à l'ID d'un patient ou bien une température à ne pas dépassé à un générateur d'énergie ou bien un moteur ect. 


## Comment amélioré la qualité d'une donnée ? DIAPO 7 :   

Dans un premier temps nous sommes tous acteur du domaine de la data, quand on créé une addresse mail ou quand contracte un abonement c'est déjà une étape de référencement de la donnée. L'utilisateur doit être conscient et vigilant des données qu'ils référence, cela va du prénom à son social ID. Mais ses aussi mettre à jour ces données, changement de numéro de téléphone, changement d'adresse ect.
A ce jour être sensibilisé et sensibliser son entourage à une meilleur contribut à une meilleure compréhension de la data et son évolution c'est un atout majeur au sein de notre société, car c'est aussi par des gestes simple que l'on peut contribué à sa qualité.

## Qu'est ce qui peut nuire à la qualité d'une donnée ? DIAPO 8 :


Désyncrhonisation d'une base de données, donc une perte l'ors d'une transaction. Une donnée tronqué, ou une mauvase gestion dite "manuel" par un opérateur data en charge du traitement de la donnée. Un piratage un bug/virus et du matériel défaillant.

Voici quelque éxemple de données qui peuvent nuire à des procédure ou à sa qualité directement: 
Une donnée remplise par défaut, une donnée absente, une donné inchoérente ou tout simplement érroné, une même donnée calculé différement ou sujette à plusieur interprétation donc impréçise ou tout simplement une donnée obsolète.

Dans le majorité des cas cela va résulté à une défaillance qui sera traduite par un temps de traitement plus long ou bien des opérations en suspens, des couts plus important dans une système financier, des mauvais conseil à un client ou encore un ciblage marketing impréçis ect..


## Cycle de vie DIAPO 10  : 

Pour revenir à son procéder, comment se déroule ce cycle de la vie d'une donnée? 

La prémière étape étant de mettre en place des contôle à différent point du cycle de la fluctuation de la donné à commencé au moment de sa collecte auprès d'une source qui pourra certifié de la qualité de cette donnée que l'on appel "GOLDEN SOURCE". Ensuite en se reférent à son modèle on va vérifié à chaque point de contrôle si les KPI sont respecté à savoir si la donnée est constante et qu'elle n'a pas était altéré.

La deuxième étape étant la gouvernance de la data qui à pour but de définir clairement la résponsabilité de chaque opérateur de la data chargé d'une procédure comme un data owner qui va réfléchir sur l'usage de cette donnée, un data designer qui va se posé sur l'architecture et enfin un data officer qui va certifié de la qualité de cette donnée. C'est donc par l'officier de la data que les déçisions seront prises. 

# One more thing 

Pour instauré ou respecter une gouvernance nous devons nous soucier également de l'intégrité d'une donnée qui représente la légalité de l'utilisation de la donnée, de la divulgué ou même de la stocker. 

Une évolution notable à prendre en compte pour le traitement de la donnée et la reforme RGPD mise en vigeur en 2018 qui se chargera de vérifié vis à vis des entreprise la conformité des données des utilisateur de son respect, sa circulation et sa divulgation. Cette reforme nous a généralement impacte depuis, vous l'avez sans doute constater mais sur différents services vous avez du réaccepter des conditions d'utilisation sur certain services. 

Il y a d'autre evolution plus spécifique comme la bcbs 239 regroupant 14 principes qui ont pour but de participer à la stabilisation du système financier mondial contraignant les banques à identifié les risques auxquelles elles sont exposées. En 2018 un deuxième réforme à été mise en vigueur, la réforme BCE anacrédit c'est un data lake européen qui contraint les banque à un reporting concéquent à un niveau nationnal pour chaque prêt contracté qui sera enfin transmis à la BCE.

{% comment %} CONCLUSION : 

UNIFORMITE UTILITE LEGALITE CONSTANCE   {% endcomment %}