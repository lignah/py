import os
from cryptography.fernet import Fernet

def load_key():
    return open("keyfile.key", "rb").read()

def decrypt_file(filepath, key):
    f = Fernet(key)
    with open(filepath, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filepath, "wb") as file:
        file.write(decrypted_data)

def main():
    key = load_key()
    for filename in os.listdir():
        if filename.endswith(".txt") and filename != "keyfile.key":
            decrypt_file(filename, key)

if __name__ == "__main__":
    main()