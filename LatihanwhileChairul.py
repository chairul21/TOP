print(25*"=")
print("Program Harga Barang")
print(25*"=")
barang = input("Nama Barang : ")
satuan = int(input("Harga Satuan : "))
ulang = int(input("Jumlah Diulang : "))
print(25*"=")
i=1
while i<=ulang:
    print(str(i),barang + " = "+str(i * satuan))
    i+=1
print(25*"=")