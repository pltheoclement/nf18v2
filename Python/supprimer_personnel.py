def supprimer_personnel(HOST, DATABASE, USER, PASSWORD):

	import psycopg2
    	
	conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
	cur = conn.cursor()

	sup = int(input("Quel est l'identifiant de la personne que vous souhaitez supprimer?"))
	

	sql = "DELETE FROM Spécialité WHERE personnel = %i ;"%(sup);
	cur.execute(sql)
	conn.commit()

	sql = "DELETE FROM Personnel WHERE id = %i ;"%(sup);
	cur.execute(sql)
	conn.commit()

	conn.close()