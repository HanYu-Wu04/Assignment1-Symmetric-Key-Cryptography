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
    padding_size = block_size - (len(data) % block_size)
    padding = bytes([padding_size]) * padding_size
    return data + padding


def pkcs7_unpad(data):
    padding_size = data[-1]

    if padding_size > len(data) or padding_size == 0:
        return data
    
    return data[:-padding_size]


def ecb_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = b""

    header = plaintext[:54]
    plaintext = plaintext[54:]

    ciphertext += header

    padded_plaintext = pkcs7_pad(plaintext, AES.block_size)

    for i in range(0, len(padded_plaintext), AES.block_size):
        block = padded_plaintext[i : i+AES.block_size]
        encrypted_block = cipher.encrypt(block)
        ciphertext += encrypted_block

    return ciphertext


def ecb_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)

    header = ciphertext[:54]
    encripted_ciphertext = ciphertext[54:]

    decrypted = b""
    for i in range(0, len(encripted_ciphertext), AES.block_size):
        block = encripted_ciphertext[i : i+AES.block_size]
        decrypted_block = cipher.decrypt(block)
        decrypted += decrypted_block

    decrypted = pkcs7_unpad(decrypted)
    decrypted_image = header + decrypted

    return pkcs7_unpad(decrypted_image)


def cbc_encrypt(plaintext, key, IV):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = b""
    previous_block = IV

    header = plaintext[:54]
    plaintext = plaintext[54:]

    ciphertext += header

    padded_plaintext = pkcs7_pad(plaintext, AES.block_size)

    for i in range(0, len(plaintext), AES.block_size):
        block = plaintext[i : i+AES.block_size]
        xor_block = bytes([b1 ^ b2 for b1, b2 in zip(block, previous_block)])
        if len(xor_block) % AES.block_size != 0:
            xor_block = pkcs7_pad(xor_block, AES.block_size)
        encrypted_block = cipher.encrypt(xor_block)
        ciphertext += encrypted_block
        previous_block = encrypted_block
        
    return ciphertext


def cbc_decrypt(ciphertext, key, IV):
    block_size = AES.block_size
    cipher = AES.new(key, AES.MODE_ECB)
    
    header = ciphertext[:54]
    ciphertext = ciphertext[54:]

    plaintext = b""
    plaintext += header

    blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
    
    for i in range(len(blocks)):
        decrypted_block = cipher.decrypt(blocks[i])
        if i == 0:
            decrypted_block = bytes([decrypted_block[j] ^ IV[j] for j in range(block_size)])
        else:
            decrypted_block = bytes([decrypted_block[j] ^ blocks[i-1][j] for j in range(block_size)])

        plaintext += decrypted_block
    
    return plaintext


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