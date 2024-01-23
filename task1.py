# task1 : Modes of Operation
# Ethan Swenke and HanYu Wu
# CSC-321-03
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def take_input(input_file):
    try:
        with open(input_file, 'rb') as file_in:
            content = file_in.read()
            ECB_content = ECB(content)
            CBC_content = CBC(content)

        with open("ECB_out", 'w') as ECB_out:
            # write ECB encryption to file
            ECB_out.write(ECB_content)

        with open("CBC_out", 'w') as CBC_out:
            # write CBC encryption to file
            CBC_out.write(CBC_content)

    except Exception as e:
        print(f"An error occurred: {e}")
        
def ECB(content):
    key = key()
    cipher = AES.new(key, AES.MODE_ECB)
    # divide the content string into blocks of 128 bits
    # check if block is full 128 bits, if not add padding()
    # run the encrypt, add that block to a new string
        # try encrypting the string itself, if not just create a new
        # empty string to add the encrypted block to
    #return the final string entirely encrypted

    encrypted_text = cipher.encrypt(content)
    return encrypted_text

def CBC(content):
    # create an IV in order to XOR with the initial block of plaintext
    # encrypt that block with the key (after checking for padding)
    # add that encryption to the result string
    # use that encrypted block to XOR with the next block of plaintext, after padding

    return

def key():
    return get_random_bytes(16)

def pkcs7_padding(block):
    # given a block of plaintext,
    # the amount of bytes needed to be padded is (16 - (len(block) % 16)
    # the value of the added bytes will also be the number of bytes padded from the above formula
    # since file read in rb, the data is in bytes. check the length with regard to this, and 
    # concatenate based on the above rules and return the new block

    return