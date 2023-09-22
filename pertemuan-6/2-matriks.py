for baris in range(4):
    for kolom in range(4):
        print("*", end=" ")
    print()

#output
# * * * * 
# * * * * 
# * * * * 
# * * * *

ukuran = 4

print("2. ==================")
for baris in range(ukuran):
    for kolom in range(ukuran-baris):
        print("*", end=" ")
    print()

print("8. ==================")
for baris in range(ukuran):
    for kolom in range(ukuran):
        if ukuran-kolom-1 > baris:
            print(" ", end=" ")
        else:
            print("*",end=" ")
        
    print()

# print("3. ==================")
# for baris in range(ukuran):
#     for kolom in range(ukuran):
#         if kolom >= baris:
#             print("*", end=" ")
#     print()

# print("4. ==================")
# for baris in range(ukuran):
#     print("* "*(ukuran - baris))

print("5. ==================")
for baris in range(ukuran):
    for kolom in range(ukuran):
        if kolom < baris:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

print("6. ==================")
for baris in range(ukuran):
    for kolom in range(baris+1):
        print("*", end=" ")
        
    print()




# print("9. ==================")
# for baris in range(1,ukuran+1):
#     print("  "*(ukuran - baris), end="")
#     print("* "*(baris) )


print("7. ==================")
for baris in range(ukuran):
    for kolom in range(ukuran):
        if kolom >= baris:
            print("*", end=" ")
        else:
            print("",end=" ")
        
    print()