import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("keyfile.key", "wb") as keyfile:
        keyfile.write(key)
    return key

def load_key():
    return open("keyfile.key", "rb").read()

def encrypt_file(filepath, key):
    f = Fernet(key)
    with open(filepath, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filepath, "wb") as file:
        file.write(encrypted_data)

def main():
    key = generate_key()
    for filename in os.listdir():
        if filename.endswith(".txt") and filename != "keyfile.key":
            encrypt_file(filename, key)

if __name__ == "__main__":
    main()