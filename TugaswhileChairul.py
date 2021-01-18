print(25*"=")
print("Program Hitung Deret")
print(25*"=")
hasil=0
nilai = int(input("Nilai N : "))

print(25*"=")
i=1
while i in range (1,nilai+1):
    print (i, end= '')
    if i== nilai:
        print ('=', end= '')
    else :
        print ('+', end= '')
    hasil = hasil + i
    print(hasil)
    i+=1
print(25*"=")
