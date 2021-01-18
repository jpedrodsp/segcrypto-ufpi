# Hash Algorithm: MD5

import hashlib
from datetime import datetime
from base64 import b64encode, b64decode

def hashtext(text: bytes) -> (datetime, str):
    start = datetime.now()
    hashed = hashlib.md5(text).hexdigest()
    end = datetime.now()
    return (end - start), hashed

def checkhash(text: bytes, hashtarget: str) -> bool:
    start = datetime.now()
    validity = False
    hashed = hashlib.md5(text).hexdigest()
    if hashed == hashtarget:
        validity = True
    end = datetime.now()
    return (end - start), validity

if __name__ == "__main__":
    print("Testing...")
    text = b"hello, world"
    htime, htext = hashtext(text)    
    ctime, cvalue = checkhash(text, htext)
    #print(htime.microseconds, htext)
    #print(ctime.microseconds, cvalue)