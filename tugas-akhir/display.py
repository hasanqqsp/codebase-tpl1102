import shutil
terminal_width, _ = shutil.get_terminal_size()

def truncate_string(input_str, max_length, align='center'):
    if len(input_str) > max_length:
        return input_str[:(max_length - 2) ] + '..|'
    else:
        return f'{input_str:^{max_length}}|' 
    

def create_row(values,calculated_cell_width,table_width, header =False, align='center'):
    print('-' * table_width) if header else None
    print('|', end='')
    values = list(map(lambda x : str(x),values))
    for idx, cell_values in enumerate(values):
        
        print(truncate_string(cell_values,calculated_cell_width[idx],align=align),end="")

    print('\n','-' * table_width,sep="")

def calculate_table_width(column,table_width):
    total_column = len(column.keys())
    reserved_width = (total_column + 1) + sum([i for i in column.values()])
    reserved_column = len(list(filter(lambda item : item > 0,column.values())))
    auto_col_width = 0 if total_column == reserved_column else int((table_width - reserved_width) / (total_column-reserved_column))
    total_width = reserved_width + (auto_col_width * (total_column - reserved_column))
    return auto_col_width,total_width

def create_box(width, content, header=False,flush=False, align='center'):
    print("-" * width) if header else None
    print("|", end="")

    if align == 'left':
        print(f"{content:<{width-2}}", end="")
    elif align == 'center':
        print(f"{content:^{width-2}}", end="")
    elif align == 'right':
        print(f"{content:>{width-2}}", end="")

    print("|")
    print("-" * width) if (not flush) else None   

def print_menu():
    menu = ['[A] Tambah Keinginan','[D] Hapus Keinginan', '[E] Ubah Keinginan','[V] Ubah Status','[R] Muat Ulang','[F] Cari','[S] Urutkan', '[N] Halaman Selanjutnya', '[P] Halaman Sebelumnya', '[X] Kembali / Logout']
    print(*menu)
    
