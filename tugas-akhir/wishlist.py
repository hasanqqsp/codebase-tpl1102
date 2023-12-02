from data import create_record, delete_record, update_record, read_records
from utils import generate_id
import os
user_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'userdata')

def create_wish(user_id, wish):
    wishes = get_all_wish(user_id)
    last_id = 0 if len(wishes) == 0 else wishes[-1][0]
    added_wish = [int(last_id)+1,wish['name'],wish['price'], wish['target'], wish['status'], wish['link']]
    create_record(os.path.join(user_data_path,user_id + '-wishlist.txt'),added_wish)
    return added_wish
    

def delete_wish(user_id, wish_id):
    delete_record(os.path.join(user_data_path,user_id + '-wishlist.txt'),wish_id)
    return wish_id

def update_wish(user_id, wish_id, updated_wish):
    wish = [wish_id,updated_wish['name'],updated_wish['price'], updated_wish['target'], updated_wish['status'], updated_wish['link']]
    update_record(os.path.join(user_data_path,user_id + '-wishlist.txt'),wish_id,wish)
    return wish

def update_wish_status(user_id, wish_id):
    wish = get_wish(user_id,wish_id)
    wish = [wish[0],wish[1],wish[2],wish[3],False if wish[4] == 'True' else True,wish[5]]
    update_record(os.path.join(user_data_path,user_id + '-wishlist.txt'),wish_id,wish)
    return wish

def get_wish(user_id, wish_id):
    records = read_records(os.path.join(user_data_path,user_id + '-wishlist.txt'))
    for i, record in enumerate(records):
        if record[0] == wish_id:
            return records[i]
        
def get_all_wish(user_id):
    return read_records(os.path.join(user_data_path,user_id + '-wishlist.txt'))

