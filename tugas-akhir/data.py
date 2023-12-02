import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'storage/users.txt')
user_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'userdata')

def add_file_if_not_exist(user_id):
    userfile = os.path.join(user_data_path,f'{user_id}-wishlist.txt')
    if not os.path.exists(userfile):
        open(userfile,'w').close()

def create_record(filename, record):
    with open(filename, 'a', newline='') as file:
        file.write(','.join(map(str, record)) + '\n')

def read_records(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    csv_data = [line.strip().split(',') for line in lines]
    return csv_data

def update_record(filename, record_id, updated_record):
    records = read_records(filename)
    for i, record in enumerate(records):
        if record[0] == record_id:
            records[i] = updated_record
            break
    print(records,record_id)
    with open(filename, 'w', newline='') as file:
        for record in records:
            file.write(','.join(map(str, record)) + '\n')

def delete_record(filename, record_id):
    records = read_records(filename)
    records = [record for record in records if record[0] != record_id]

    with open(filename, 'w', newline='') as file:
        for record in records:
            file.write(','.join(record) + '\n')
def delete_file(user_id):
    userfile = os.path.join(user_data_path,f'{user_id}-wishlist.txt')

    if os.path.exists(userfile):
        os.remove(userfile)

    userfile = os.path.join(user_data_path,f'{user_id}-wishlist.txt')

