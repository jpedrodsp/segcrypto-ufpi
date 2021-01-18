# Asymmetric algorithm: RSA

import Crypto
from Crypto.PublicKey import RSA
from datetime import datetime
from base64 import b64encode, b64decode
import utils

def crypt(text: bytes, publickey):
    start = datetime.now()
    ciphered = publickey.encrypt(text, 32)
    end = datetime.now()
    return (end - start), ciphered

def decrypt(text: bytes, privatekey):
    start = datetime.now()
    unciphered = privatekey.decrypt(text)
    end = datetime.now()
    return (end - start), unciphered

if __name__ == "__main__":
    print("Testing...")
    privatekey = utils.read_rsa_privatekey()
    publickey = utils.read_rsa_publickey()

    ctime, ctext = crypt(b"Hello, World!", publickey)
    dtime, dtext = decrypt(ctext, privatekey)
    print(ctime.microseconds, ctext)
    print(dtime.microseconds, dtext)