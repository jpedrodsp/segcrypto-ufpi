from datetime import datetime
from datetime import timedelta
import Crypto
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

def calculate_timeresult(timediff_list):
    sum = timediff_list[0] - timediff_list[0]
    for diff in timediff_list:
        sum += diff
    average = sum / len(timediff_list)
    return average.total_seconds() * 1000, sum.total_seconds() * 1000

def read_rsa_publickey():
    fp = open("./data/rsa-publickey.txt")
    key = fp.read()
    fp.close()
    publickey = RSA.importKey(key)
    return publickey

def read_rsa_privatekey():
    fp = open("./data/rsa-privatekey.txt")
    key = fp.read()
    fp.close()
    privatekey = RSA.importKey(key)
    return privatekey

def read_aes_key():
    fp = open("./data/aes-key.txt")
    key = fp.read()
    fp.close()
    aeskey = AES.new(key)
    return aeskey

def read_textcontent():
    fp = open("./data/content.txt")
    content = fp.read()
    fp.close()
    content = bytes(content, "utf-8")
    return content
    