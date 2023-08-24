# fungsi input menerima sebuah string yang akan menjadi output, kemudian mengembalikan nilai yang berupa string dari input user
# mis
panjang = input("masukan panjang : ")
lebar =  input("masukan lebar : ")

# perlu diperhatikan bahwa nilai kembalian dari input str

# maka harus dilakukan type casting
panjang = int(panjang)
lebar = int(lebar)
print("Luas = " ,panjang * lebar ,"cm")