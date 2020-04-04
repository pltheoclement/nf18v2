#!/usr/bin/python3

import psycopg2
from ajout_animal import *
from afficher_animaux import *
from ajouter_client import *
from ajout_personnel import
from ajout_medicament import *
from afficher_medicament import *

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
    print ("2. Afficher la liste des Animaux")
    print ("3. Statistiques des Animaux traites ")
    print ("4. Statistiques des medicaments")
    print ("5. Ajouter un client")
    print ("6. Ajouter un personnel")
    print ("7. Ajouter un medicament")
    print ("8. Option 8")
    print ("9. Option 9")
    print ("10. Option 10")
    print ("11. Sortir")
     
    print ("Choisissez une option")
 
    option = nombre_entier()
 
    if option == 1:
        print ("Ajouter un Animal ")
        ajout_animal(HOST, DATABASE, USER, PASSWORD)
    elif option == 2:
        print ("Afficher Animaux:")
        afficher_animaux(HOST, DATABASE, USER, PASSWORD)
    elif option == 3:
        print ("Statistiques des Animaux traites")
        statistiques_animaux(HOST, DATABASE, USER, PASSWORD)
    elif option == 4:
        print ("Statistiques des medicaments")
        afficher_medicaments(HOST, DATABASE, USER, PASSWORD)
    elif option == 5:
        print ("Ajouter un client")
        ajout_client(HOST, DATABASE, USER, PASSWORD)
    elif option == 6:
        print ("Ajouter  Personnel ")
        ajout_personnel(HOST, DATABASE, USER, PASSWORD)
    elif option == 7:
        print ("Ajouter un medicament ")
        ajout_medicament(HOST, DATABASE, USER, PASSWORD)
    elif option == 8:
        print ("Option 8")
    elif option == 9:
        print ("Option 9")
    elif option == 10:
        print ("Option 10")
    elif option == 11:
        sortir = True
    else:
        print ("Entrez un nombre entre 1 et 10")
 
print ("Fin")