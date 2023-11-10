def fib(n,a=0,b=1,i=0):
    if n == i:
        print()
        return 
    print(a, end=" ")
    a = a + b
    
    return fib(n, b,a, i +1)
    
fib(10)

# for i in range(10):
#     print(fib(i))