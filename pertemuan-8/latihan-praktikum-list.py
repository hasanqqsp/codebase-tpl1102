# list kosong
list_kosong = []
# list yang berisi kumpulan string
list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']
# list yang berisi kumpulan integer
list_nilai = [80, 70, 90, 60]
# list campuran berbagai tipe data
list_jawaban = [150, 33.33, 'Presiden Sukarno', False]

# list_buah.insert(1,'Durian')
# list_buah.pop()
# print(list_buah)

list_buah[1:] = [str(i) for i in range(1,4)]

print(list_buah)

# print('list_kosong:', list_kosong)
# print('list_buah:', list_buah)
# print('list_nilai:', list_nilai)
# print('list_jawaban:', list_jawaban)

# print(list_buah[0])
# print(list_buah[2])
# print(list_buah[1])
# print(list_buah[3])

# print(list_buah[-1])
# print(list_buah[-2])
# print(list_buah[-3])
# print(list_buah[-4])

# print(list_buah[0:1])
# print(list_buah[0:2])
# print(list_buah[1:3])
# print(list_buah[0:-1])
# print(list_buah[-1:-3])
# print(list_buah[-1:3])
# print(list_buah[-3:-1])

# print(list_buah[0:])
# print(list_buah[1:])
# print(list_buah[2:])
# print(list_buah[3:])
# print(list_buah[:0])
# print(list_buah[:1])
# print(list_buah[:2])
# print(list_buah[:3])
# print(list_buah[:4])

# print(list_buah)

# list_buah[0] = 'Jeruk'
# # print(list_buah)

# list_buah[-1] = 'Mangga'
# # print(list_buah)

# list_buah[1:3] = ['Naga', 'Pepaya']
# print(list_buah)

# list_buah = ['Jeruk', 'Naga', 'Pepaya', 'Mangga']
# print(list_buah)

# list_buah.append('Sirsak')
# print(list_buah)

# list_buah.insert(0, 'Jambu')
# print(list_buah)

# list_buah.insert(2, 'Manggis')
# print(list_buah)

# list_angka = [1, 2, 3, 4, 5]
# print(list_angka)

# angka_yang_terhapus = list_angka.pop()
# print('angka yang terhapus:', angka_yang_terhapus)
# print(list_angka)

# list_buah = ['Mangga', 'Jambu', 'Jeruk', 'Jambu']
# print(list_buah)
# # hapus item pertama dengan nilai 'Jambu'
# list_buah.remove('Jambu')
# print(list_buah)

# list_buah = ['Mangga', 'Jambu', 'Jeruk', 'Jambu']
# print(list_buah)
# del list_buah[1]
# print(list_buah)
# del list_buah[0:2]
# print(list_buah)

# a = [1, 2, 3]
# b = ['a']
# c = [True, 'b', False]

# listBaru = a + b + c

# print(listBaru)

list_buah = ['Mangga', 'Jeruk', 'Zaitun', 'Apel', 'Durian']
print(list_buah)

list_buah.sort()
print(list_buah)

list_buah.reverse()
print(list_buah)