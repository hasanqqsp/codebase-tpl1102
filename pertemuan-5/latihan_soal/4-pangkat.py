exp = 1

bil = int(input("bil = "))
pangkat = int(input("pangkat = "))

for _ in range(pangkat):
    exp *= bil

print(bil,"^",pangkat,"=",exp)