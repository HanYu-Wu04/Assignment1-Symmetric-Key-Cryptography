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
    byte_flip_str = byte_flipping(submit_str)

    return print(verify(byte_flip_str, key, IV))


def submit(str, key, IV):
    # URL encode any ; or = characters that appear in the user provided string
        # git st; is %3B and = is %3D 
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
    
    return substr in decrypted_str[16:].decode('utf-8')


def byte_flipping(ciphertext):
    # given the ciphertext, we need to find the right bytes to flip such that
    # the plaintext that it will be xor'd with will have the corrects bytes changed
    eq_xor = ord('e') ^ ord('=')
    semi_xor = ord('s') ^ ord(';')
    ciphertext = bytearray(ciphertext)
    ciphertext[4] ^= semi_xor
    ciphertext[10] ^= eq_xor
    ciphertext[15] ^= semi_xor
    ciphertext = bytes(ciphertext)

    return ciphertext


def main():
    if len(sys.argv) != 1:
        print("Usage: python task2.py")
        return

    task2()
    

if __name__ == "__main__":
    main()