# task2 : Limits of Confidentiality
# Ethan Swenke and HanYu Wu
# CSC-321-03
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def submit(str):
    # URL encode any ; or = characters that appear in the user provided string
    # pad this new string using PCKS#7
    # encrypt this string using our CBC implemenation

    res_str = "userid=456; userdata=" + str + ";session-id=31337"
    return res_str

def verify(str):
    # decrypt the encrypted string
    # parse the string for the patter ";admin=true;"
    # return true / false based on whether that string is present
    
    return

def generate_key():
    return get_random_bytes(16)

def pkcs7_pad(data, block_size):
    padding_size = block_size - (len(data) % block_size)
    padding = bytes([padding_size] * padding_size)
    return data + padding

def main():
    if len(sys.argv) != 2:
        print("Usage: python task2.py <input_str>")
        return

    input_str = sys.argv[1]
    

if __name__ == "__main__":
    main()