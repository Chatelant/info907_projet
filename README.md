# Info 907 : Projet

Le script python genère une page index.html affichant un graph de connaissance portant sur des studios, leurs genres et animes associés.

## Utilisation du programme

Pour utilisé ce programme, il faut passer plusieurs paramaètre:
- Le premier paramètre correspond à la source (`wikidata` ou `dbpedia`)
- Le second paramètre correspond au numéro de la requête à executer

## Description de chaque numéro:
- 1. Affiche la liste des nom d'animé
- 2. Affiche la liste des noms de studios, ainsi que les noms d'animé qu'ils ont réalisé
- 3. Affiche les genres d'animé réalisé par chaque studio (ne fonctionne pas sur dbpedia
- 4. Affiche les noms des animé originaux fait par chaque studio (ne fonctionne pas sur wikidata)

## Exemple d'utilisation

```
py main.py wikidata 1
```

```
py main.py dbpedia 2
```


