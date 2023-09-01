x1, y1, x2, y2 = input().split()

x = int(x1) - int(x2)
y = int(y1) - int(y2)

x = x if x > 0 else -1 * x
y = y if y > 0 else -1 * y

print(x+y)