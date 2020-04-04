def afficher_animaux(HOST, DATABASE, USER, PASSWORD):

	import psycopg2
    	
	conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
	cur = conn.cursor()

	sql = "SELECT * FROM animaux ORDER BY nom";
	cur.execute(sql)


	
	row = cur.fetchone()

	while row:

		print("NUM_DOSSIER: %s  NOM: %s  DATE_NAISS: %s  NUM_PUCE: %s  NUM_PASSEPORT: %s ESPECE: %s" % (row[0], row[1], row[2], row[3], row[4], row[5]))
		row = cur.fetchone()

	conn.close()