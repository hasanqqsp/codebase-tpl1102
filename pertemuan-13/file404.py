# with open("dataku.txt", "r") as file:
#     print(file.read())

try:
    with open("dataku.txt", "r") as file:
        print(file.read())
except:
    print("File gak ada")