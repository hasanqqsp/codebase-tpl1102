from display import create_box, create_row, calculate_table_width,print_menu
from utils import clear
from data import read_records,create_record, add_file_if_not_exist
from users import register, login, delete_account
from forms import create_wish_form,delete_wish_form, update_wish_form,get_keyword_form, change_wish_status_form, get_sortby_form
from wishlist import create_wish,get_all_wish, delete_wish, update_wish, update_wish_status
import shutil,os, sys
from datetime import datetime
terminal_width, _ = shutil.get_terminal_size()
import math
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'storage/users.txt')

headers = {
    "#": 5,
    'ID': 5,
    'Nama Barang' : 40,
    'Harga' : 16,
    'Target':12,
    'Status' : 11,
    'Link' :0,
}
row1 = [1, 'Galaxy Tab S9 FE', f'{6900000:,}','01-01-2024','✔','https://www.samsung.com/id/tablets/galaxy-tab-s9-fe/buy/']
row2 = [2, 'MacBook Pro (16.2 inci, M1, 2021) 10C CPU, 16C GPU, 1TB”', f'{6900000:,}','01-08-2024','×','https://ibox.co.id/product/macbook-pro-16-2-inci-m1-2021-10c-cpu-16c-gpu-1tb-space-grey']
    
def map_data(enum):
    idx, item = enum
    return [idx+1, item[0],item[1],'{:,}'.format(int(item[2])).replace(',', '*').replace('.', ',').replace('*', '.'),item[3][0:10],'✔' if item[4] == "True" else '×',item[5]]

def create_table(columns,body,keyword="",auto=True,table_width=100):
    table_width = terminal_width if auto else table_width
    auto_col_width, total_width = calculate_table_width(columns,table_width)
    
    calculated_cell_width = list(map(lambda cell_width : auto_col_width if cell_width == 0 else cell_width,columns.values()))
    create_row(columns.keys(),calculated_cell_width,total_width,header=True)
    body = list(map(map_data,enumerate(body)))
    if len(body) == 0:
        if keyword == "":
            create_box(table_width,'Belum ada keinginan ditambahkan')
        else:
            create_box(table_width,f'Tidak keinginnan ditemukan dengan keyword \'{keyword}\'')

    for i in body:
        create_row(i,calculated_cell_width,total_width)


def front_page():
   
        create_box(40,"my WISHLIST",header=True)
        create_box(40,"",flush=True)
        create_box(40,"  Menu",flush=True,align="left")
        create_box(40,"  1. Register",flush=True,align="left")
        create_box(40,"  2. Login",flush=True,align="left")
        create_box(40,"  3. Delete Account",flush=True,align="left")
        create_box(40,"  4. Exit",flush=True, align="left")
        create_box(40,"")
    

def main():
    clear()
    users_lists = read_records(file_path)
    authenticated_user = None
    used = True
    interactive = True

    while used:
        
        if authenticated_user == None:
            try:
                front_page()
                choice = input("Masukan Pilihan anda (1-4): ")

                if choice == '1':
                    clear()
                    user_data = register(users_lists)
                    clear()
                    authenticated_user = user_data
                    users_lists = read_records(file_path)
                    continue


                elif choice == '2':
                    clear()
                    user = login(users_lists)
                    authenticated_user = user
                    if user:
                        continue

                elif choice == '3':
                    clear()
                    if (delete_account(users_lists)):

                        used = False
                        input()
                        sys.exit()
                    else:
                        continue
                        

                elif choice == '4':
                    clear()
                    create_box(80, "", header=True,flush=True)
                    for i in range(5):
                        create_box(80, "", header=False,flush=True)
                    create_box(80, "Terimakasih sudah menggunakan my WISHLIST", header=False,flush=True)
                    create_box(80, "Semoga keinginan anda dapat tercapai", header=False,flush=True)
                    create_box(80, "Enter untuk kembali ke terminal", header=False,flush=True)

                    for i in range(5):
                        create_box(80, "", header=False,flush=True)
                    create_box(80, "", header=False,flush=False)
                    
                    used = False
                    input()
                else:
                    clear()
                    print("Pilihan Salah, Silakan Coba Lagi")
                    continue
            except KeyboardInterrupt:
                clear()
                create_box(80, "", header=True,flush=True)
                for i in range(5):
                    create_box(80, "", header=False,flush=True)
                create_box(80, "Terimakasih sudah menggunakan my WISHLIST", header=False,flush=True)
                create_box(80, "Semoga keinginan anda dapat tercapai", header=False,flush=True)
                create_box(80, "Enter untuk kembali ke terminal", header=False,flush=True)

                for i in range(5):
                    create_box(80, "", header=False,flush=True)
                create_box(80, "", header=False,flush=False)
                
                used = False
                input()
        else :
            mode = 'w'
            page = 1
            keyword = ''
            sortby = 0
            reverse = True
            interactive = True
            def sort_by_key(data, key):
                return sorted(data, key=lambda x: int(x[key]) if key == 0 or key == 2 else x[key])
            
            while interactive:
                print(f"Welcome, {authenticated_user[1]}!")
                add_file_if_not_exist(authenticated_user[0])
                user_input = None
                print("mode : ", mode)
                wishes = get_all_wish(authenticated_user[0])
                
                if not keyword == '':
                    wishes = [item for item in wishes if (keyword in item[1].lower())]
                    print("Filtered by keyword : ",keyword)
                wishes = sort_by_key(wishes,sortby)
                if reverse:
                    wishes.reverse()

                total_page = math.ceil(len(wishes)/10)
                this_page = wishes[((page-1)*10):((page-1)*10) + 10]

                if mode == 'w':
                    create_table(headers,this_page,keyword)
                    if page > total_page and total_page != 0:
                        page = total_page
                        continue
                    print(f"[Halaman {page} dari {total_page}]")
                    print_menu()
                    user_input = input()
                    mode = user_input.lower()

                elif mode == 'a':
                    data = create_wish_form()
                    if data:
                        create_wish(authenticated_user[0],data)
                    mode = 'w'

                elif mode == 'd':
                    id = delete_wish_form(wishes)
                    if id:
                        delete_wish(authenticated_user[0],id)
                    mode = 'w'

                elif mode == 'e':
                    data = update_wish_form(authenticated_user[0],wishes)
                    if data:
                        update_wish(authenticated_user[0],data["id"],data)
                    mode = 'w'    


                elif mode == 'n':
                    if page < total_page:
                        page += 1
                    mode = 'w'
                    clear()

                elif mode == 'p':
                    if not page == 1:
                        page -= 1
                    mode = 'w'
                    clear()

                elif mode == 'r':
                    keyword = ''
                    mode = 'w'
                    clear()

                elif mode == 'f':
                    keyword = get_keyword_form()
                    if keyword:
                        mode = 'w'
                    clear()

                elif mode == 'v':
                    id = change_wish_status_form()
                    if id:
                        update_wish_status(authenticated_user[0],id)
                    mode = 'w'
                    clear()

                elif mode == 's':
                    s = get_sortby_form()
                    if s:
                        sortby,reverse = s
                    mode = 'w'
                    clear()
                    

                elif mode == 'x':
                    clear()
                    interactive = False
                    authenticated_user = None
                else :
                    mode = 'w'
                    clear()
                    print("Pilihan Mode tidak valid")
        
if __name__ == "__main__":
    main()