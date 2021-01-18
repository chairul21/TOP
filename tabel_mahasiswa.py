import mysql.connector
db = mysql.connector.connect (
host="localhost",
user="root",
passwd="",
database="data_mahasiswa"
)
cursor = db.cursor()
sql = """CREATE TABLE mahasiswa (
NPM VARCHAR(20) PRIMARY KEY,
Name VARCHAR(50),
Email VARCHAR(50),
Phone VARCHAR(20)
)
"""
cursor = db.cursor()
print("Tabel berhasil dibuat!")