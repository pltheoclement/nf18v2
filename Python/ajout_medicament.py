def ajout_medicament(HOST, DATABASE, USER, PASSWORD):

    import psycopg2

    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    cur = conn.cursor()

    molecule = input("Molecule : ")
    effets  = input("Effets : ")


    try:
        sql = "INSERT INTO Médicaments (molecule, effets) VALUES ('%s', '%s')"% (molecule, effets)
        cur.execute(sql)
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print ("Erreur, message système : ", e)

    conn.close()
