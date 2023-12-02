import os
import getpass

from utils import is_username_taken, hash_password,generate_id,clear
from display import create_box
from data import create_record, delete_file, delete_record

user_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'userdata')
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'storage/users.txt')

def register(users_list):
    try:
        print("Selamat datang di aplikasi registrasi!")
        ok = False
        while not ok:
            username = input("Masukkan username: ").strip().lower()
            full_name = input("Masukkan nama lengkap: ")
            password = getpass.getpass("Masukkan password: ")
            if not (username and full_name and password):
                print("Tidak boleh ada yang dikosongkan")
                print("Silakan Ulangi \n")
                continue

            if len(password) < 6:
                print("Password minimal 6 karakter")
                print("Silakan Ulangi \n")
                continue

            if (is_username_taken(username,users_list)):
                print("Username sudah digunakan")
                print("Silakan Ulangi \n")
                continue
            ok = True

        
        if ok:
            hashed_password = hash_password(password)
            id = generate_id()
            
            open(os.path.join(user_data_path,id + '-wishlist.txt'),'w').close()
            user_data = [id, full_name, username ,hashed_password]
            create_record(file_path,user_data)

            print("Registrasi berhasil!")
            return user_data
    except KeyboardInterrupt:
        clear()
        return


def login(users):
    while True:
        try:
            create_box(40,"Login:",header=True)
            username = input("Enter your username: ")
            username = username.lower().strip()
            password = getpass.getpass("Enter your password: ")
            for user in users:
                if user[2] == username and user[3] == hash_password(password):
                    clear()
                    return user

            clear()
            print("Invalid username or password. Please try again.")
        except KeyboardInterrupt:
            clear()
            return
    

def delete_account(users):
    while True:
        try:
            print("Masukan username dan password untuk menghapus akun:")
            print("-"*40)
            username = input("Enter your username: ")
            username = username.lower()
            password = getpass.getpass("Enter your password: ")
            for user in users:
                if user[2] == username and user[3] == hash_password(password):
                    clear()
                    delete_file(user[0])
                    delete_record(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'storage/users.txt'),user[0])
                    create_box(80, "", header=True,flush=True)
                    for i in range(3):
                        create_box(80, "", header=False,flush=True)
                    create_box(80, "Akun Berhasil Dihapus", header=False,flush=True)

                    for i in range(3):
                        create_box(80, "", header=False,flush=True)
                    create_box(80, "", header=False,flush=False)
                    return True
            else:
                print("User dan/atau password salah")


            clear()
            print("Invalid username or password. Please try again.")
        except KeyboardInterrupt:
            clear()
            return
    
