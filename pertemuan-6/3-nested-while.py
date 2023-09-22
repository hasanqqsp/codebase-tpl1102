ukuran_baris = 5
ukuran_kolom = 5

baris = 0
while(baris<ukuran_baris):
    kolom = 0
    while kolom < ukuran_kolom:
        if(baris >= kolom):
            print('o', end=" ")
        else:
            print('+', end=" ")
        kolom +=1
    baris +=1
    print()