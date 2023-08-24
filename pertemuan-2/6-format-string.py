# #print dapat diubah separatornya dengan menambahkan keyword arguments sep (secara default " " (spasi))
# # mis
# print("Aku", "Cinta", "Dia", sep=" - ") # output : "Aku - Cinta - Dia"
# #print dapat diubah akhirnya dengan menambahkan keyword arguments sep
# # mis
# print("Aku", end="-")
# print("Cinta", end="+")
# print("Dia")
# #output Aku-Cinta+Dia

#menggunakan method str.format dari <class:str> https://docs.python.org/3/library/stdtypes.html#str.format

print('{} + {} = {}'.format(5, 3, 5+3)) #output : "5 + 3 = 8"

# bisa juga menambahkan index
print('{1} dan {0}'.format("Saya", "Dia")) # output : "Dia dan Saya"

# bisa juga menggunakan keyword argument
print('{namaBelakang}, {namaDepan}'.format(namaDepan = "Hasan", namaBelakang = "Ismail")) # output : "Ismail, Hasan"

