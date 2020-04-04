def afficher_medicaments(HOST, DATABASE, USER, PASSWORD):
	
	c = 0

	import psycopg2
    	
	conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
	cur = conn.cursor()

	sql = "SELECT molecule, effets FROM médicaments ORDER BY molecule";
	cur.execute(sql)


	print("\n\n")

	row = cur.fetchone()

	while row:

		print("MOLECULE: %s  EFFETS: %s " % (row[0], row[1]))
		row = cur.fetchone()
		c += 1

	print("\nLe nombre de médicaments dans la clinique est: %i\n\n" % (c))

	conn.close()