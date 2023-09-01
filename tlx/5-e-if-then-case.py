angka = int(input())
if angka > 99999 or angka <= 0:
    pass
elif(angka > 9999):
    print("puluhribuan")
elif (angka > 999):
    print("ribuan")
elif (angka > 99):
    print("ratusan")
elif (angka >  9):
    print("puluhan")
else:
    print("satuan")
