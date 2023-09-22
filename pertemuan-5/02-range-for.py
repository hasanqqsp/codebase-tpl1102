sampai5 = range(5) # range mengembalikan immutable sequence of number sebanyak stop
satu_sampai_5 = range(1,6) # mengembalikan immutable sequence of number dari start (argumen pertama) sampai sebelum stop (argumen kedua)
bil_genap = range(2,11,2) # mengembalikan immutable sequence of number dari start sampai sebelum stop dengan selisih step
for i in range(5):
    print(i) #output : 0, 1, 2, 3, 4

for i in range(5,11):
    print(i) #output : 5, 6, 7, 8, 9,

for i in range(2,10,2):
    print(i) #output : 2, 4, 6, 8

for i in range(1,10,2):
    print(i) #output : 1, 3, 5, 7, 9

for i in range(1,10):
    i % 2 == 1 and print(i) #output : 1, 3, 5, 7, 9

i = 0
iterator = iter(sampai5)
while i < len(sampai5):
    print(next(iterator))
    i += 1