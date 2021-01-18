import mysql.connector
db = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="data_mahasiswa"
)
cursor = db.cursor()
sql = "INSERT INTO mahasiswa (NPM, Name, Email, Phone) VALUES (%s, %s, %s, %s)"
values = [
("202011","Soledad Wiyoko", "soledad@gmail.com", "08123456789"),
("200413","Hadirman Koto", "hardiman@gmail.com", "08123456789"),
("201056","Joko Lelana", "lelana@gmail.com", "08123456789"),
("201171","Enrico Silaban", "enricos@gmail.com", "08123456789")
]
for val in values:
    cursor.execute(sql, val)
db.commit()
print("{} data ditambahkan".format(len(values)))