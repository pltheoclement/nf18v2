#!/usr/bin/python3

import psycopg2
import ajout_animal

HOST = "tuxa.sme.utc"
USER = "********"
PASSWORD = "********"
DATABASE = "db********"

conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
 
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
 
    print ("1. Option 1")
    print ("2. Option 2")
    print ("3. Option 3")
    print ("4. Option 4")
    print ("5. Option 5")
    print ("6. Option 6")
    print ("7. Option 7")
    print ("8. Option 8")
    print ("9. Option 9")
    print ("10. Option 10")
    print ("11. Sortir")
     
    print ("Choisissez une option")
 
    option = nombre_entier()
 
    if option == 1:
        print ("Option 1")
    elif option == 2:
        print ("Option 2")
    elif option == 3:
        print ("Option 3")
    elif option == 4:
        print ("Option 4")
    elif option == 5:
        print ("Option 5")
    elif option == 6:
        print ("Option 6")
    elif option == 7:
        print ("Option 7")
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

conn.close()