import pymssql
conn = pymssql.connect(host='daanvanmeerthema10.database.windows.net', port=1433,
database='Thema10', user='daanvanmeer', password='DitIsEenWachtwoord123!a')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Klant;')
row = cursor.fetchone()
while row:
 #Doe iets met deze rows
 print(str(row[0]) + ' \t' + str(row[1]) + ' ' + str(row[2]) + ' ' + str(row[3]) + ' ' + str(row[4]))
 row = cursor.fetchone()

conn.commit()
conn.close() 