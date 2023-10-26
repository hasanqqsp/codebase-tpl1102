# list adalah sebuah tipe data terurut yang bersifat mutable
# list dapat memiliki tipe data yang tercampur
# Tipe data ini bisa kita definisikan dengan tanda kurung siku [] di dalam Python.

daftar_angka = [1,3,5,7,'8']
# Catatan : sebaiknya anda tidak membuat list di variable bernama list list 
# list dapat dicetak ke console dengan

print(daftar_angka) # [1, 3, 5, 7, '8']

# argument bintang akan memecah tiap tiap elemen dalam list sehingga menjadi argument bagi sebuah fungsi
print(*daftar_angka, sep="-") # 1-3-5-7-8

# menampilkan dan slicing (memotong)

print(daftar_angka[1]) # Output : 3
# daftar_angka[x] akan mengambil angka pada index ke x

print(daftar_angka[-1]) # Output : 8
# daftar_angka[-x] akan mengambil angka pada index ke x dari belakang
# NB: yang perlu diperhatikan adalah: bahwa indeks negatif tidak dimulai dari 0, akan tetapi
# dimulai dari angka 1.

# memotong
print(daftar_angka[0:2])
# daftar_angka[x,y] akan mengambil angka pada index ke x sampai y-1

print(daftar_angka[0:-1])
# daftar_angka[x,-y] akan mengambil angka pada index ke x sampai sebelum y angka terakhir dari kana 

print(daftar_angka[-3:])
# daftar_angka[-x] akan mengambil x angka paling belakang (tidak terbalik)

print(daftar_angka[-1:-4:-1])
# daftar_angka[-1:-y] akan mengambil y-1 angka paling belakang terbalik