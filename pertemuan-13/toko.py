print('APLIKASI KASIR TOKO ALAT TULIS')
pensil = input('Pembelian pensil = ')
hapusan = input('Pembelian penghapus = ')
buku = input('Pembelian buku = ')
beli = int(pensil)*1000 + int(hapusan)*500 + int(buku)*2000
print('Pembelian = Rp',beli)
data = open('penjualan.txt','r')
penjualan = int(data.read())
data.close()
total = penjualan + beli
print('Total penjualan = Rp',total)
data = open('penjualan.txt','w')
data.write(str(total))
data.close()