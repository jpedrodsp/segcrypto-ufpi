# Symmetric algorithm: AES

import Crypto
from Crypto.Cipher import AES
from datetime import datetime
from base64 import b64encode, b64decode
import utils

def crypt(text: bytes, aeskey):
    start = datetime.now()
    ciphered = aeskey.encrypt(text)
    end = datetime.now()
    return (end - start), ciphered

def decrypt(text: bytes, aeskey):
    start = datetime.now()
    unciphered = aeskey.decrypt(text)
    end = datetime.now()
    return (end - start), unciphered

if __name__ == "__main__":
    print("Testing...")
    aeskey = utils.read_aes_key()
    strcontent = utils.read_textcontent()
    ctime, ctext = crypt(strcontent, aeskey)
    dtime, dtext = decrypt(ctext, aeskey)
    
    print("Crypt elapsed time: {}".format(ctime.microseconds))
    print("Crypt result: {}".format(ctext))
    print("Decrypt check elapsed time: {}".format(dtime.microseconds))
    print("Decrypt result: {}".format(dtext))