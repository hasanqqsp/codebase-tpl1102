# 7, jumlah keduanya 7 selisih 7

bil_1 = int(input("Masukkan integer pertama : "))
bil_2 = int(input("Masukkan integer kedua   : "))

salah_satu = bil_1 == 7 or bil_2 == 7
jumlah_keduanya = bil_1 + bil_2 == 7
selisih = bil_1 - bil_2 == 7 or bil_2 - bil_1 == 7

if salah_satu or jumlah_keduanya or selisih:
    print("Hasil : Benar")
else:
    print("Hasil : Salah")