# Description
# Pak Dengklek baru saja mengajarkan bebek-bebeknya mengenai deret bilangan. Sekarang Pak
# Dengklek akan memberikan sebuah bilangan bulat N, Pak Dengklek meminta bebek-bebeknya
# menuliskan deret penjumlahan dari 1 sampai N beserta hasil penjumlahan deret tersebut.
# Input Format
# Masukan terdiri dari sebuah baris yang berisi sebuah bilangan bulat N, bilangan yang disebutkan
# oleh Pak Dengklek.
# Output Format
# Keluaran terdiri dari dua baris. baris pertama berisi deret yang seharusnya dituliskan oleh bebekbebek Pak Dengklek. baris kedua adalah penjumlahan dari deret tersebut. Perhatikan contoh
# keluaran.
# Sample Input
# 5
# Sample Output
# 1+2+3+4+5
# 15

angka = int(input())
statement = ''
jumlah = 0
for i in range(1,angka+1):
    jumlah +=i
    statement += str(i)
    statement += '+' if i != angka else ''

print(statement,jumlah,sep='\n')
