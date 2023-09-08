from math import sqrt

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
det = b ** 2 - 4 * a * c
x1 = (-1 * b + sqrt(det)) / (2 * a)
x2 = (-1 * b - sqrt(det)) / (2 * a)

print(x1, x2)