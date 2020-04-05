def ajout_personnel(HOST, DATABASE, USER, PASSWORD):

    import psycopg2
    
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    cur = conn.cursor()



    nom = input("Nom : ")
    prenom = input("Prenom : ")

    print ("Date de naissance : ")
    erreur = False
    while (not erreur):
        try:
            JNaiss = int(input("    Jour : "))
            MNaiss = int(input("    Mois : "))
            ANaiss = int(input("    Année : "))
            erreur = True
        except:
            print ("Erreur, veuillez entrer des entiers positifs")

    adresse = input("Adresse : ")


    tel = int(input("Telephone : "))

    nposte = int(input("Quelle est son poste? Tapez 1 pour Vétérinaire, 2 pour Assistant : "))
		
    if nposte == 1:
        poste = "vétérinaire"
    if nposte == 2:
        poste = "assistant"	


    try:
        sql = "INSERT INTO personnel (nom, prenom, dtNaiss, adresse, tel, poste) VALUES ('%s','%s', '%i-%i-%i', '%s', %i, '%s')"% (nom, prenom, ANaiss, MNaiss, JNaiss, adresse, tel, poste)
        cur.execute(sql)
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print ("Erreur, message système : ", e)

    conn.close()
    
    
    
def afficher_personnel(HOST, DATABASE, USER, PASSWORD):

	import psycopg2

	conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
	cur = conn.cursor()

	sql = "SELECT * FROM personnel ORDER BY nom";
	cur.execute(sql)

	row = cur.fetchone()

	while row:

		print("ID: %s  NOM: %s  PRENOM: %s  DATE DE NAISSANCE: %s  ADRESSE: %s  TEL: %s  POSTE: %s" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
		row = cur.fetchone()

	conn.close()
