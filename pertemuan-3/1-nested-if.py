nilai = int(input("nilai: "))
usia = int(input("usia: "))

if nilai >= 75:
    if(usia <  15):
        print("Selamat adek, kamu lulus!")
    else:
        print("Selamat kakak, kamu lulus!")
else:
    if(usia <  15):
        print("Mohon maaf dek, coba lagi ya!")
    else:
        print("Mohon maaf kak, coba lagi ya!")

# Kode diatas dapat diubah kedalam bentuk lain (tanpa menggunakan percabangan bersarang)

if nilai >=  75 and usia < 15:
    print("Selamat adek, kamu lulus!")
elif nilai >=  75 and not(usia < 15):
    print("Selamat kakak, kamu lulus!")
elif not (nilai >=  75) and usia < 15:
    print("Mohon maaf dek, coba lagi ya!")
else:
    print("Mohon maaf kak, coba lagi ya!")