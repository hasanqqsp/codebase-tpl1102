a = 2
b = 3
c = -4

# Setelah baris tersebut diberikan kode berikut apa yang dihasilkan

print(a<b<=c)
# print((a<b) and (b<=c))
# sama dengan (a<b) and (b<=c)
# output : False 

#print(a=b=c) # menghasilkan error karena assignment tidak bisa di print
print(a!=b!=c) 
# sama dengan (a!=b) and (b!=c)
# output :True 
# print(a + "kali") # menghasilkan error karena int tidak bisa langsung ditambah dengan string

print(a * "kali ")
# Outputnya adalah "kali kali"
# method perkalian diimplementasikan untuk string
