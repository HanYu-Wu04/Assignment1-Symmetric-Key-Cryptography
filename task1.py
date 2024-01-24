# task1 : Modes of Operation
# Ethan Swenke and HanYu Wu
# CSC-321-03
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys

def generate_key():
    return get_random_bytes(16)

def generate_iv():
    return get_random_bytes(16)

def pkcs7_pad(data, block_size):
    # given a block of plaintext,
    # the amount of bytes needed to be padded is (16 - (len(block) % 16)
    # the value of the added bytes will also be the number of bytes padded from the above formula
    # since file read in rb, the data is in bytes. check the length with regard to this, and 
    # concatenate based on the above rules and return the new block
    padding_size = block_size - (len(data) % block_size)
    padding = bytes([padding_size] * padding_size)
    return data + padding

def pkcs7_unpad(data):
    # the last byte of the data is the number of bytes padded
    # check the last byte, and remove that many bytes from the end of the data
    padding_size = data[-1]
    if padding_size > len(data):
        raise Exception("Invalid padding...")
    return data[:-padding_size]

def ecb_encript(plaintext, key):
    # divide the content string into blocks of 128 bits
    # check if block is full 128 bits, if not add padding()
    # run the encrypt, add that block to a new string
        # try encrypting the string itself, if not just create a new
        # empty string to add the encrypted block to
    #return the final string entirely encrypted
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pkcs7_pad(plaintext, AES.block_size))
    return ciphertext

def ecb_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = pkcs7_unpad(cipher.decrypt(ciphertext))
    return decrypted

def cbc_encrypt(plaintext, key, IV):
    # create an IV in order to XOR with the initial block of plaintext
    # encrypt that block with the key (after checking for padding)
    # add that encryption to the result string
    # use that encrypted block to XOR with the next block of plaintext, after padding
    cipher = AES.new(key, AES.MODE_CBC, IV)
    ciphertext = b""
    previous_block = IV
    for i in range(0, len(plaintext), AES.block_size):
        block = plaintext[i:i + AES.block_size]
        xor_block = bytes([b1 ^ b2 for b1, b2 in zip(block, previous_block)])
        encrypted_block = cipher.encrypt(pkcs7_pad(xor_block, AES.block_size))
        ciphertext += encrypted_block
        previous_block = encrypted_block
    return ciphertext

def cbc_decrypt(ciphertext, key, IV):
    cipher = AES.new(key, AES.MODE_CBC, IV)
    decrypted = pkcs7_unpad(cipher.decrypt(ciphertext))
    return decrypted

def read_bmp_file(file_name):
    with open(file_name, 'rb') as file_in:
        content = file_in.read()
    return content

def write_bmp_file(file_name, content):
    with open(file_name, 'wb') as file_out:
        file_out.write(content)

def write_encrypted_file(file_name, content):
    with open(file_name, 'wb') as file_out:
        file_out.write(content)

def task1(file_path):
    plaintext = read_bmp_file(file_path)

    key = generate_key()
    IV = generate_iv()

    output_ecb_file = 'output_ecb.bmp'
    output_cbc_file = 'output_cbc.bmp'

    ECB_ciphertext = ecb_encript(plaintext, key)
    CBC_ciphertext = cbc_encrypt(plaintext, key, IV)
    write_encrypted_file("ecb_encrypted.bmp", ECB_ciphertext)
    write_encrypted_file("cbc_encrypted.bmp", CBC_ciphertext)

    decrypted_ECB = ecb_decrypt(ECB_ciphertext, key)
    write_bmp_file("decrypted_ecb.bmp", decrypted_ECB)

    decrypted_CBC = cbc_decrypt(CBC_ciphertext, key, IV)
    write_bmp_file("decrypted_cbc.bmp", decrypted_CBC)

def main():
    if len(sys.argv) != 2:
        print("Usage: python task1.py <input_bmp>")
        return

    input_bmp = sys.argv[1]
    task1(input_bmp)

if __name__ == "__main__":
    main()