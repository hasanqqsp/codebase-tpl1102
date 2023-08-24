# Operator : simbol khus menjalankan operasi tertentu (logika / aritmatika)
# Operan : nilai yang dioperasikan operator mis : a + b , a dan b adalah operan

# Operator aritmatika
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

# shorthand operasi aritmatika

# mis 
c = 15

c += 2

# maka nilai c menjadi 17
print(c)

# shorthand berlaku untuk operator lainnnya -=, *=, /=, %=, dll

# operator perbandingan yang menghasilkan boolean ( > , <, >=, <=, ==, !=)

print ( 5 < 5 ) # output : False
print ( 5 <= 5 ) # output : True
print ( 5 != 5 ) # output : False

# operator logika (and, or, not)

print (True or False) # output : True
print (False and True) # output : False
print (not False) # output : True

# Operator keanggotaan, khusus untuk tipe data sequence (tuple, dict, list)

a = [10,4,2]
print(type(a)) # output : <class 'list'>
print (10 in a) # output : True
print (1 in a) # output : False

# Operator identitas, untuk mengecek apakah operan identik dalam penempatan dalam memory

d = 5
e = 5
f = [1,2,3]
g = [1,2,3]

print ( d is e ) # output : True
print (f[1] is g[1]) # output : True

