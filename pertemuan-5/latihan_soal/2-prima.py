bil = int(input("bil = "))

for angka in range(2,bil):
    if bil % angka == 0:
        print(bil,"bukan bilangan prima")
        break
else:
    print(bil,"adalah bilangan prima")

