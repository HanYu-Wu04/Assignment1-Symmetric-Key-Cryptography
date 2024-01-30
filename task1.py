# task1 : Modes of Operation
# Ethan Swenke and HanYu Wu
# CSC-321-03
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import sys


def generate_key():
    return get_random_bytes(16)


def generate_iv():
    return get_random_bytes(16)


def pkcs7_pad(data, block_size):
    padding_size = block_size - (len(data) % block_size)
    padding = bytes([padding_size] * padding_size)

    return data + padding


def pkcs7_unpad(data):
    padding_size = data[-1]

    if padding_size >= len(data):
        raise Exception("Invalid padding...")
    
    return data[:-padding_size]


def ecb_encrypt(plaintext, key):
    plaintext = pkcs7_pad(plaintext, AES.block_size)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = b""

    for i in range(0, len(plaintext), AES.block_size):
        block = plaintext[i : i+AES.block_size]
        encrypted_block = cipher.encrypt(block)
        ciphertext += encrypted_block

    return ciphertext


def ecb_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = pkcs7_unpad(cipher.decrypt(ciphertext))

    return decrypted


def cbc_encrypt(plaintext, key, iv):
    plaintext = pkcs7_pad(plaintext, AES.block_size)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = b""
    previous_block = iv

    for i in range(0, len(plaintext), 16):
        block = plaintext[i:i+16]
        xor_block = bytes([b1 ^ b2 for b1, b2 in zip(block, previous_block)])
        encrypted_block = cipher.encrypt(xor_block)
        ciphertext += encrypted_block
        previous_block = encrypted_block

    return ciphertext


def cbc_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = b""
    previous_block = iv

    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i+16]
        decrypted_block = cipher.decrypt(block)
        decrypted_block = bytes([b1 ^ b2 for b1, b2 in zip(decrypted_block, previous_block)])
        decrypted_text += decrypted_block
        previous_block = block

    return pkcs7_unpad(decrypted_text)


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

    ECB_ciphertext = ecb_encrypt(plaintext, key)
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