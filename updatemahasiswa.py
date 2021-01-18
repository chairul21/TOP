import mysql.connector
db = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="data_mahasiswa"
)
cursor = db.cursor()
sql = "UPDATE mahasiswa SET Phone=%s, Name=%s, Email=%s WHERE NPM=%s"
val= ("087827163832", "Soledad Jatmiko", "soledad@gmail.com", 202011 )
val= ("082391283121", "Hardiman Koto", "hardimank@gmail.com", 200413 )
val= ("082391283121", "Jaka Kelana", "jkelana@gmail.com", 201056 )
val= ("089822110182", "Enrico Silalahi", "enricosil@gmail.com", 201171 )
cursor.execute(sql, val)  
db.commit()
print("{} data diubah".format(cursor.rowcount))