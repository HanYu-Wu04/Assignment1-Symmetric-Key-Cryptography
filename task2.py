# task2 : Limits of Confidentiality
# Ethan Swenke and HanYu Wu
# CSC-321-03
import sys
from Crypto.Random import get_random_bytes
from urllib.parse import quote
from task1 import *


def task2():
    IV = generate_key()
    key = generate_key()
    user_input = input("Enter a string: ")
    submit_str = submit(user_input, key, IV)

    return print(verify(submit_str, key, IV))


def submit(str, key, IV):
    # URL encode any ; or = characters that appear in the user provided string
        # in ASCII, ; is %3B and = is %3D 
    # pad this new string using PCKS#7
    # encrypt this string using our CBC implemenation
    str = quote(str)
    app_str = "userid=456;userdata=" + str + ";session-id=31337"
    encrypted_str = cbc_encrypt(app_str.encode('utf-8'), key, IV)

    return encrypted_str


def verify(str, key, IV):
    # decrypt the encrypted string
    # parse the string for the pattern ";admin=true;"
    # return true / false based on whether that string is present
    substr = ";admin=true;"
    decrypted_str = cbc_decrypt(str, key, IV)
    print(decrypted_str)
    
    return substr in decrypted_str.decode('utf-8')


def main():
    if len(sys.argv) != 1:
        print("Usage: python task2.py")
        return

    task2()
    

if __name__ == "__main__":
    main()