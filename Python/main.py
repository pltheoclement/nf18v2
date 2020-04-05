#!/usr/bin/python3

import psycopg2
from ajout_animal import *
from afficher_animaux import *
from ajout_client import *
from ajout_personnel import *
from ajout_medicament import *
from afficher_medicament import *
from supprimer_personnel import*
from saisir_taille import *
from saisir_poids import *

HOST = "tuxa.sme.utc"
USER = "********"
PASSWORD = "********"
DATABASE = "db********"

def nombre_entier():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Entrez un entier:"))
            correcto=True
        except ValueError:
            print('Erreur, entrez un entier')
     
    return num
 

sortir = False
option = 0
 
while not sortir:
 
    print ("1. Ajouter un Animal")
    print ("2. Ajouter un client")
    print ("3. Ajouter un personnel")
    print ("4. Ajouter un medicament")
    print ("5. Afficher la liste des Animaux")
    print ("6. Statistiques des Animaux traites")
    print ("7. Afficher la liste du personnel")
    print ("8. Saisir la taille d'un animal")
    print ("9. Supprimer personnel")
    print ("10. Saisir le poids d'un animal")
    print ("11. Sortir")
     
    print ("Choisissez une option")
 
    option = nombre_entier()
 
    if option == 1:
        print ("Ajouter un Animal ")
        ajout_animal(HOST, DATABASE, USER, PASSWORD)
    elif option == 2:
        print ("Ajouter un client")
        ajout_client(HOST, DATABASE, USER, PASSWORD)
    elif option == 3:
        print ("Ajouter un personnel")
        ajout_personnel(HOST, DATABASE, USER, PASSWORD)
    elif option == 4:
        print ("Ajouter un medicament")
        ajout_medicament(HOST, DATABASE, USER, PASSWORD)
    elif option == 5:
        print ("Afficher la liste des animaux (ordre alphabétique)")
        afficher_animaux(HOST, DATABASE, USER, PASSWORD)
    elif option == 6:
        print ("Statistiques des animaux traites ")
        statistiques_animaux(HOST, DATABASE, USER, PASSWORD)
    elif option == 7:
        print ("Afficher la liste du personnel (ordre alphabétique)")
        afficher_personnel(HOST, DATABASE, USER, PASSWORD)
    elif option == 8:
        print ("Saisir la taille d'un animal")
        saisir_taille(HOST, DATABASE, USER, PASSWORD)
    elif option == 9:
        print ("Supprimer personnel")
        supprimer_personnel(HOST, DATABASE, USER, PASSWORD)
    elif option == 10:
        print ("Saisir le poids d'un animal")
        saisir_poids(HOST, DATABASE, USER, PASSWORD)
    elif option == 11:
        sortir = True
    else:
        print ("Entrez un nombre entre 1 et 10")
 
print ("Fin")