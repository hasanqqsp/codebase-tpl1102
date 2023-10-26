# sebuah_list =  ['Zorin OS',
#  'Ubuntu',
#  'FreeBSD',
#  'NetBSD',
#  'OpenBSD',
#  'Backtrack',
#  'Fedora',
#  'Slackware']

# sebuah_tuple = (0,1,2,3,4,5,6,7,8,9)

# sebuah_dictionary = {
#     'nama' : 'Hasan Ismail Abdulmalik',
#     'prodi':'Teknologi Rekayasa Perangkat Lunak',
#     'email' : 'hasanabdulmalik@apps.ipb.ac.id',
#     'website' : 'https://github.com/hasanqqsp'
# }

# print(sebuah_list)
# print(sebuah_tuple)
# print(sebuah_dictionary)

# print("mengakses salah satu elemen : ")
# print("-----------------------------")
# print(sebuah_list[5])
# print(sebuah_tuple[8])
# print(sebuah_dictionary['website'])

# print("mengakses beberapa elemen : ")
# print("-----------------------------")
# print(sebuah_list[2:5])

# print(sebuah_tuple[3:6])


# # sebanyak 3 elemen terakhir
# print(sebuah_list[-3:])

# # sebanyak 3 elemen awal
# print(sebuah_list[:3])

# # urutan ke empat
# print(sebuah_list[4])


# list kosong
list_kosong = []
# list yang berisi kumpulan string
list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']
# list yang berisi kumpulan integer
list_nilai = [80, 70, 90, 60]
# list campuran berbagai tipe data
list_jawaban = [150, 33.33, 'Presiden Sukarno', False]

print(list_buah[-1])
print(list_buah[-2])
print(list_buah[-3])
print(list_buah[-4])

# Output : 
# Durian
# Melon
# Nanas
# Pisang

print(list_buah[0:1])
print(list_buah[0:2])
print(list_buah[1:3])
print(list_buah[0:-1])
print(list_buah[-1:-3])
print(list_buah[-1:3])
print(list_buah[-3:-1])

# Output:
# ['Pisang']
# ['Pisang', 'Nanas']
# ['Nanas', 'Melon']
# ['Pisang', 'Nanas', 'Melon']
# []
# []
# ['Nanas', 'Melon']