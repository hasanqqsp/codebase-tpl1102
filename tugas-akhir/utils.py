import hashlib
import secrets
import os
def clear():
    os.system("clear")

def generate_id():
    # Generate a secure random 16-byte ID and convert it to a hexadecimal string
    id_number = secrets.token_hex(8)
    return id_number


def hash_password(password):
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the bytes of the password
    hash_object.update(password.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_password = hash_object.hexdigest()

    return hashed_password

def is_username_taken(username, users):
    # Iterasi melalui users untuk memeriksa keberadaan username
    for user in users:
        if user[2] == username:
            return True  # Username sudah digunakan
    return False