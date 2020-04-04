def ajout_animal(HOST, DATABASE, USER, PASSWORD):

    import psycopg2

    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    cur = conn.cursor()

    nom = input("Nom : ")

    print ("Date de naissance :")
    erreur = False
    while (not erreur):
        try:
            JNaiss = int(input("    Jour : "))
            MNaiss = int(input("    Mois : "))
            ANaiss = int(input("    Année : "))
            erreur = True
        except:
            print ("Erreur, veuillez entrer des entiers positifs")

    numPuce = 0
    puce = int(input("Voulez vous ajouter un numéro de puce ? Tapez 1 pour oui, 2 pour non : "))
    if puce == 1:
        erreur = False
        while (not erreur):
            try:
                numPuce = int(input("Numéro de la puce : "))
                erreur = True
            except:
                print ("Erreur, veuillez entrer un entier positif")

    numPasseport = 0
    passeport = int(input("Voulez vous ajouter un numéro de passeport ? Tapez 1 pour oui, 2 pour non : "))
    if passeport == 1:
        erreur = False
        while (not erreur):
            try:
                numPasseport = int(input("Numéro du passeport : "))
                erreur = True
            except:
                print ("Erreur, veuillez entrer un entier positif")

    erreur = False
    while (not erreur):
        try:
            espece = input("Espèce (felin, canide, reptile, rongeur, oiseau ou autre) : ")
            assert espece == 'felin' or espece == 'canide' or espece == 'reptile' or espece == 'rongeur' or espece == 'oiseau' or espece == 'autre'
            erreur = True
        except AssertionError:
            print ("Erreur, veuillez entrer une valeur parmi celles proposées")

    try:
        sql = "INSERT INTO animaux (nom, dtNaiss, numPuce, numPasseport, espece) VALUES ('%s', '%i-%i-%i', %i, %i, '%s')"% (nom, ANaiss, MNaiss, JNaiss, numPuce, numPasseport, espece)
        cur.execute(sql)
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print ("Erreur, message système : ", e)

    conn.close()
