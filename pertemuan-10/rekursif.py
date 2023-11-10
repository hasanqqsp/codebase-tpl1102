#Step 3 : Panggil diri sendiri
# def tampilkanAngka (batas, i = 1):
#     print(f'Perulangan ke {i}')
#     if (i < batas):
#         tampilkanAngka(batas, i + 1)

# tampilkanAngka(10)

# def tampilkanAngka (batas, i = 1):
#     if (i < batas):
#         tampilkanAngka(batas, i + 1)
#     print(f'Perulangan ke {i}')

# tampilkanAngka(10)

def tampilkanAngka (batas, i = 1):
    prefix = '--' * (i - 1)
    print(f'{prefix} Sebelum rekursif ({i})')
    if (i < batas):
        tampilkanAngka(batas, i + 1)
        print(f'{prefix} Setelah rekursif ({i})')

tampilkanAngka(5)

# #Step 2 : Tentukan batasan
# def tampilkanAngka (batas, i = 1):
#     print(f'Perulangan ke {i}')

# tampilkanAngka(3)
# tampilkanAngka(3, 2)
# tampilkanAngka(3, 3)


# def tampilkanAngka (i):
#     print(f'Perulangan ke {i}')
 
    
# tampilkanAngka(1)
# tampilkanAngka(2)
# tampilkanAngka(3)


# def tampilkanAngka (batas, i = 1):
#     prefix = '--' * (i - 1)
#     print(f'{prefix} Sebelum rekursif ({i})')
#     if (i < batas):
#         # di sini lah rekursifitas itu terjadi
#         tampilkanAngka(batas, i + 1)
#         print(f'{prefix} Setelah rekursif ({i})')
#         # memanggil fungsi tampilkanAngka
#         # untuk pertama kali

# tampilkanAngka(5)