for i in range(0,5):
    if (i == 2):
        continue # skip to next sequence , baris dibawah tidak dieksekusi
    print(i) #output : 0, 1, 3, 4 

for i in range(0,5):
    if (i == 2):
        break # menghentikan looping, baris dibawahnya juga tidak dieksekusi
    print(i) #output : 0, 1