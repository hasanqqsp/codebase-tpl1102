listKota = ['Jakarta', 'Surabaya','Depok', 'Bekasi', 'Yogyakarta','Surakarta']

while len(listKota) > 0: # sebuah list, collection, atau iterable bernilai Falsy (setara kondisi false ketika kosong)
    print(listKota.pop(-1)) # pop akan menghapus array index tertentu, mengembalikan nilai dan menghapus dari list
    print(listKota) # -1 bermaksud array terakhir