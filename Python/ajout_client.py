def ajout_client(HOST, DATABASE, USER, PASSWORD):

    import psycopg2

    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    cur = conn.cursor()

    nom = input("Nom : ")
    prenom = input("Prenom : ")
    adresse = input("Adresse : ")

    print ("Date de naissance :")
    erreur = False
    while (not erreur):
        try:
            JNaiss = int(input("    Jour (JJ) : "))
            MNaiss = int(input("    Mois (MM) : "))
            ANaiss = int(input("    Année (AAAA) : "))
            erreur = True
        except:
            print ("Erreur, veuillez entrer des entiers positifs")

    erreur = False
    while (not erreur):
        try:
            tel = int(input("Numéro de téléphone (sans espaces) : "))
            assert tel > 100000000 and tel < 1000000000
            erreur = True
        except AssertionError:
            print ("Erreur, veuillez entrer un numéro de téléphone valide")

    try:
        sql = "INSERT INTO Clients (nom, prenom, dtNaiss, adresse, tel) VALUES ('%s', '%s', '%i-%i-%i', '%s', %i)"% (nom, prenom, ANaiss, MNaiss, JNaiss, adresse, tel)
        cur.execute(sql)
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print ("Erreur, message système : ", e)

    conn.close()
