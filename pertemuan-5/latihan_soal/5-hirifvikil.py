kalimat = input("kalimat = ")
vokal = input("vokal = ")
kalimat_baru = ''
for char in kalimat:
    if char.lower() in 'aiueo':
        kalimat_baru +=  vokal
    else: 
        kalimat_baru += char
print(kalimat_baru)
