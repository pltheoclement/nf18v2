from afficher_animaux import *

def saisir_taille(HOST, DATABASE, USER, PASSWORD):

    import psycopg2

    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    cur = conn.cursor()

    afficher_animaux(HOST, DATABASE, USER, PASSWORD)

    erreur = False
    while (not erreur):
        try:
            numDossier = int(input("Numéro de dossier de l'animal parmi ceux ci-dessus : "))
            erreur = True
        except:
            print ("Erreur, veuillez entrer un entier positif")

    erreur = False
    while (not erreur):
        try:
            mesure = int(input("Mesure de la taille (en cm) : "))
            erreur = True
        except:
            print ("Erreur, veuillez entrer un entier positif")

    print ("Date de saisie :")
    erreur = False
    while (not erreur):
        try:
            JSaisie = int(input("    Jour : "))
            MSaisie = int(input("    Mois : "))
            ASaisie = int(input("    Année : "))
            erreur = True
        except:
            print ("Erreur, veuillez entrer des entiers positifs")

    try:
        sql = "INSERT INTO Taille VALUES (%i, '%i-%i-%i', %i)"% (mesure, ASaisie, MSaisie, JSaisie, numDossier)
        cur.execute(sql)
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print ("Erreur, message système : ", e)


    conn.close()
