from utils import clear
from datetime import datetime
from wishlist import get_wish

import sys
def create_wish_form():
    clear()
    complete = False
    while not complete:
        try:
            print("Tambahkan keinginanmu disini")
            print("-"*40)
            name = input("Nama Barang: ")
            if not name:
                raise 'no name'
            price = int(input("Harga Barang: "))
            target = datetime.strptime(input("Target Terbeli (DD-MM-YYYY): "),'%d-%m-%Y')
            link = input("Tautan: ")
            complete = True
            return {"name": name, "price": price, "target": target, "link": link, "status" :False}
            
        except KeyboardInterrupt:
            return
        except:
            clear()
            print("Isian tidak sesuai silakan ulangi")
            continue



def update_wish_form(user_id,wishes):
    clear()
    complete = False
    id = None
    while not complete:
        try:
            print("Masukan ID keinginan yang akan diubah")
            print("-"*40)
            ids = list(map(lambda x : x[0],wishes))
            print(ids)
            id = input("ID: ")
            # if id not in ids :
            #     raise "no id"
            complete = True
        except KeyboardInterrupt:
            return
        except:
            clear()
            print("ID tidak valid atau tidak ditemukan")
            continue
    old_value = get_wish(user_id, id)
    complete = False
    while not complete:
        try:
            print("Ubah keinginanmu disini")
            print("Tekan enter jika tidak ada perubahan")
            print("-"*40)
            name = input(f'Nama Barang [{old_value[1]}] : ') or old_value[1]
            
            price = input(f'Harga Barang [{"{:,}".format(int(old_value[2])).replace(",", "*").replace(".", ",").replace("*", ".")}] : ') or old_value[2]
            dt = datetime.strptime(old_value[3][0:10],'%Y-%m-%d')
            target = datetime.strptime(input(f"Target Terbeli [{datetime.strftime(dt,'%d-%m-%Y')}] : ") or datetime.strftime(dt,'%d-%m-%Y'),'%d-%m-%Y')
            link = input(f'Tautan [{old_value[5]}] : ') or old_value[5]
            complete = True
            return {"id": id,"name": name, "price": price,
                    "target": target, "status": old_value[4], "link": link}
        except KeyboardInterrupt:
            sys.exit()
        except:
            clear()
            print("Isian tidak sesuai silakan ulangi")
            continue
            


def delete_wish_form(wishes):
    clear()
    complete = False
    while not complete:
        try:
            print("Masukan ID keinginan yang akan dihapus")
            print("-"*40)
            ids = list(map(lambda x : x[0],wishes))
            print(ids)
            id = input("ID: ")
            if id not in ids :
                raise "no id"
            complete = True
            return id
        except KeyboardInterrupt:
            return
        except:
            clear()
            print("ID tidak valid atau tidak ditemukan")
            continue

def get_keyword_form():
    clear()
    
    print("Cari berdasarkan nama barang")
    print("-"*40)
    keyword = input("Cari Barang: ")
 
    return keyword

def get_sortby_form():
    try:
        clear()
        while True:
            print("Urutkan Keinginan : ")
            print("-"*40)
            print(" 1. Nama Barang")
            print(" 2. Harga Barang")
            
            sortby = input("Pilih : ")
            if not (sortby == '1' or sortby == '2'):
                continue
            
            
            reversed = input("ASCENDING / DESCENDING [1 / 0] :" ) 
            if not (reversed == '1' or reversed == '0'):
                continue
            reversed = False if reversed == '1' else True

            return int(sortby), reversed
    except KeyboardInterrupt:
        return
        
            
def change_wish_status_form():
    try:
        clear()
        
        print("Ubah status keinginan")
        print("-"*40)
        id = input("ID Barang: ")
    
        return id
    except KeyboardInterrupt:
        return