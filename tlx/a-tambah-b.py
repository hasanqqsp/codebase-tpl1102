import functools

angka = input().split(" ")
print(functools.reduce(lambda a,b : int(a)+int(b),angka))