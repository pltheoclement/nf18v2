<h1 align="center"> NOTE DE CLARIFICATION <\h1> <br>

**INTEGRANTS**

* DOUALE Clement
* LEDOUX Matteo
* TETARD PIerre
* ZUNIGA Uriel
* PEREZ Steven

<hr>

<h2 align="center"> CONTEXTE ET OBJECTIFS <\h2>

Ce projet de NF18 vise à développer une gestion d'une clinique vétérinaire. 
Le gestionnaire de la clinique veut pouvoir ajouter et mettre à jour la liste des personnels, des clients, des animaux traités et les médicaments utilisés. Il doit aussi pouvoir obtenir facilement des rapports d'activité et des informations statistiques, comme les quantités de médicaments consommés, le nombre de traitement ou de procédure effectuées dans la clinique, ou encore des statistiques sur les espèces d'animaux traités.
Ces informations seront présentées sous la forme d’une base de données, dans laquelle elles seront stockées. 


<hr>

<h2 align="center"> LIVRABLES <\h2> <br> 


 Livrables v1 () 
<br>

- README (avec les noms des membres du groupe)
- Analyse du besoin de l’utilisateur - Note de clarification
- MCD
- MLD relationnel
- La base de données : tables, données de test, questions attendues
- Application Python

Livrables v2 ()
<br>

- Actualisation - Note de clarification
- MCD
- MLD relationnel
- La base de données  : tables et vues, données de test, questions attendues (vues)
- Application Python


Nous reprendrons l'ensemble de votre projet afin :

*De corriger les erreurs relevées dans la v2 <br>
De refaire votre conception afin d'intégrer : héritage, contraintes, composition, vues, requêtes statistiques (agrégats), normalisation, transaction et optimisation<br>
De l'augmenter de nouvelles fonctions (+25%)*

<hr>



<h2 align="center"> DÉTAILS DU SYSTÈME </h2> <br> 

Nous cherchons à représenter différents objets au sein d'une base de données afin d'organiser la clinique vétérinaire.

Les differents objects qu'on veut répresenter sont:

* les clients
* les personals soignants
* les animaux
* les medicaments
* les dossiers medicaux


<h4> Le client </h4> <br> 

- Nom
- Prénom
- Date de naissance
- Numéro de téléphone
- Adresse

<h4> Les personals soignants </h4> <br> 

- Nom
- Prénom
- Date de naissance
- Numéro de téléphone
- Adresse
- Spécialité

<h4> Animal  </h4> <br> 

- Nom
- Espèce: félin, canidé, reptile, rongeur, oiseau, autre
- Date de naissance
- Numéro  de puce d'identification
- Numéro de passeport

<h4> Le médicament </h4> <br>


- nom de molécule
- ensemble d’effets

<h4> Dossier médical  </h4> <br>


Le poids:

            Mesure
            Date et une heure 

La taille: 

            Mesure
            Date et une heure 

La consultation:

            Date de consultation
            Observation
            Personnel effectuant la consultation
            Date et heure

Le traitement:

            Date de début
            Durée
            Date de saisie dans la base de données


Un traitement ne peut être prescrit que par un vétérinaire de la clinique et comprend un à plusieurs médicaments.

L’analyse

            Résultat
            Date 


Un patient peut ne pas avoir eu d’analyses pendant son suivi.

La procédure

            Nom
            Description
            Date et heure

