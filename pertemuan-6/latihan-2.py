# Task 8 : Pigura
# Description
# Sekarang Anda diminta untuk membuat sebuah pigura bermodalkan sebuah karakter berupa
# huruf abjad dan sebuah digit angka. Pigura yang akan dibentuk mempunyai pola sebagai berikut:
# • Digit yang diberikan akan dituliskan pada sel-sel yang berada di tepi
# • Jika terdapat sel tengah, tuliskan dengan karakter '*'
# • Tuliskan huruf pada sel-sel yang tersisa

# Pigura setidaknya berukuran 2 × 2.
# Input Format
# Baris pertama berisi sebuah bilangan bulat K yang menyatakan ukuran sisi pigura.
# Baris kedua berisi sebuah karakter C.
# Baris ketiga berisi sebuah digit D.
# Output Format
# Keluaran terdiri dari K baris, yang masing-masing berisi tepat K karakter, sesuai penjelasan pada
# deskripsi soal.
# Sample Input
# 5
# a
# 8
# Sample Output
# 88888
# 8aaa8
# 8a*a8
# 8aaa8
# 88888
K = int(input())
C = input()
D = input()
tengah = None if K % 2 == 0 else K // 2 + 1    

for baris in range(1,K+1):
    for kolom in range(1,K+1):
        if(baris==1 or kolom == 1 or baris == K or kolom == K):
            print(D,end="")
        elif(baris == tengah and kolom == tengah):
            print("*",end="")
        else:
            print(C,end="")
    print()
    
