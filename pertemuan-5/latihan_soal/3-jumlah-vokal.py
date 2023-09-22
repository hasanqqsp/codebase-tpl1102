jumlah_vokal = 0
kata = input("kata = ")
for i in kata:
    if i.lower() in 'aiueo':
        jumlah_vokal += 1

print(jumlah_vokal)
