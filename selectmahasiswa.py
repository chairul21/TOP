import mysql.connector
db = mysql.connector.connect (
host="localhost",
user="root",
passwd="",
database="data_mahasiswa"
)
cursor = db.cursor()
sql = "SELECT * FROM mahasiswa"
cursor.execute(sql)
results = cursor.fetchall()
for data in results:
    print(data)