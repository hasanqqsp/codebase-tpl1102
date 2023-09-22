# Task 9 : Bilangan Elegan
# Suatu bilangan dikatakan elegant jika banyak faktor/pembaginya adalah 4. Sebagai contoh, 10
# adalah bilangan elegant (karena ia punya 4 faktor yaitu 1, 2, 5, dan 10) sementara 9 bukan bilangan
# elegan (karena ia punya 3 faktor yaitu 1, 3, dan 9).
# Input Format
# Masukan terdiri dari sebuah bilangan N
# Output Format
# Keluaran berupa pernyataan bahwa bilangan N tersebut bilangan elegan atau tidak
# Sample Input
# 10
# Sample Output
# Bilangan elegan
# Sample Input
# 9
# Sample Output
# Bukan Bilangan elegan

bilangan = int(input())
jumlah_faktor_pembagi = 0
for i in range(1,bilangan+1):
    if bilangan % i == 0:
        jumlah_faktor_pembagi += 1

print('Bilangan elegan' if jumlah_faktor_pembagi == 4 else 'Bukan Bilangan elegan')
