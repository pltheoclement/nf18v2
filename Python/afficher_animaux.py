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
	
def statistiques_animaux(HOST, DATABASE, USER, PASSWORD):

	c_feline = 0
	c_canide = 0
	c_reptile = 0
	c_rongeur = 0
	c_oiseau = 0
	c_autre = 0
	c_total = 0

	import psycopg2
    	
	conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
	cur = conn.cursor()

	sql = "SELECT * FROM animaux ORDER BY nom";
	cur.execute(sql)
	
	row = cur.fetchone()

	while row:

		c_total += 1

		if (row[5] == 'felin'):
			c_feline += 1
		elif(row[5] == 'canide'):
			c_canide += 1
		elif(row[5] == 'reptile'):
			c_reptile += 1
		elif(row[5] == 'rongeur'):
			c_rongeur += 1
		elif(row[5] == 'oiseau'):
			c_oiseau += 1
		elif(row[5] == 'autre'):
			c_autre += 1

		row = cur.fetchone()
	

	print("\n\nLe nombre total des animaux traités: % i \n - Felins : %i \n - Canides: %i \n - Reptile: %i \n - Rongeur: %i \n - Oiseau: %i \n - Autres: %i \n\n" % (c_total, int(c_feline),int(c_canide), int(c_reptile), int(c_rongeur), int(c_oiseau), int(c_autre)))

	conn.close()