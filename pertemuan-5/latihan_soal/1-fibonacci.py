n = int(input("n = "))

fib = 0
nmin1 = 1
nmin2 = 0
cache = 0

for i in range(n):
    nmin2 = nmin1
    nmin1 = fib
    fib = nmin1 + nmin2
    print(fib,end=" ")

print()
