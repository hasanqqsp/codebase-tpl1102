# Buatlah program menghitung
# Jumlah bilangan yang ada pada list
# Penjumlahan bilangan yang ada pada list

# daftar_angka = [1,2,3,4,5]
# count = 0
# sum = 0
# for angka in daftar_angka:
#     count += 1
#     sum += angka
# else:
#     print(count)
#     print(sum)

daftar_angka = [1,2,3,4,5]
jumlah = 0
for index, angka in enumerate(daftar_angka):
    jumlah += angka
    
else:
    print(index + 1)
    print(jumlah)