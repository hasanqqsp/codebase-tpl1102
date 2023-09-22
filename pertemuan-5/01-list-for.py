listKota = ['Jakarta', 'Surabaya','Depok', 'Bekasi', 'Yogyakarta','Surakarta']

for kota in listKota:
    print(kota)

for enum_kota in enumerate(listKota):
    print(enum_kota) # output : (1, 'Surabaya'), (2, 'Depok'), (3, 'Bekasi')
    print(type(enum_kota)) # output : <class 'tuple'>, <class 'tuple'>, <class 'tuple'>,...
    print(enum_kota[0]) # 0, 1, 2, 3, ...
    print(enum_kota[1]) # 'Jakarta', 'Surabaya','Depok', 'Bekasi', ...
