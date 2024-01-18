# task1 : Modes of Operation
# Ethan Swenke and HanYu Wu
# CSC-321-03
from Crypto.Random import AES

def take_input(input_file):
    try:
        with open(input_file, 'r') as file_in:
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

# need to implement our own:
    # PKCS#7 padding for files that are not evenly divisible by 128 bits
        # http://tools.ietf.org/html/rfc5652#section-6.3
        # http://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7 
    # key generation

def ECB(content):
    return

def CBC(content):
    return

def key():
    return