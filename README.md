# Data

## Content

It's provided a example content with size of `128 bytes`. This is a restriction of `hashlib` `md5` library. It's filepath is in: `data/content.txt`
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Heh!
```

## Keys
- RSA public/private key pair.

Filepath: `data/rsa-publickey.txt`, `data/rsa-privatekey.txt`
- AES key (32 bytes).

Filepath: `data/aes-key.txt`

# Asymmetric (RSA) algorithm

## Instructions 
Please generate a pair of RSA keys (public and private), and put them on path:
- `data/rsa-publickey.txt`
- `data/rsa-privatekey.txt`

## Example private key
```rsa
-----BEGIN RSA PRIVATE KEY-----
MIICWgIBAAKBgGcjT6/asMjkLUQFp5IK3k9zAV5nTurMSWEDzeVji8poI+tasSY9
Bf47n80S7t866DxCC5L0bfKvgJ13fPB/XWOK86hlQEPCsEAYH9iqGpKQRYqTpec/
6PqJEQsi6zSfbuLG0+GMhAep7STIwS9rxh6OQfVkMg1c375VerioqCPJAgMBAAEC
gYA3MhWWViIgEMUMzz3jkX9x42lLHVyFmbh3e/K3nXOVafA3Jz0A6s2HRl95/3To
8HySqwHIrpkctMHPA8BQcMkIKptuAOlZwnO13eBQOVd/qKpD5K4/9kZ1Mt1+C/ZT
Wg8aYROBukZmqOxpaCZiwJ7+YKuC2tRVpe/VPdXYfog1EQJBALaj6xfwmXMB1PLX
tqSurHi5BZbcc/LS+C8fymeV0z+2wqrfnEpWHGOH0JxCUOkLgHXa6KurnHnkNPX7
D7KD5n0CQQCQkIV/iJBZlS0R89mSvZq/98/GJwMrScrl47p0dPfqDDjWTNEf7mVR
+pl5bAJVm6eqtoo5xouOMXI5C+x14Jg9AkAY+b1yXqJ9SajXNIxzZLeNIrAS+z6X
3CW4O/6vv5tNwS5Js55pw/DJ446xb5gk5j/A3hinMSaKvJxJbvWskcD5AkA7ZrcE
JWgy9yIS22EOc8xPjxMX99XMhsDRX5aw3ZM035rHK79OYJXPbqp7gw8egBwQAHuh
q9ySK+0kVaru8L99AkBUbL18R+WoT9GUCYszZjzE34ZLNzVIQrfBu8nFm3J2P1ir
Kjt5aJle6ExvhKMtf0HMXPu7eQ4YhsCUtEFAQtJT
-----END RSA PRIVATE KEY-----
```

## Example public key
```rsa
-----BEGIN PUBLIC KEY-----
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgGcjT6/asMjkLUQFp5IK3k9zAV5n
TurMSWEDzeVji8poI+tasSY9Bf47n80S7t866DxCC5L0bfKvgJ13fPB/XWOK86hl
QEPCsEAYH9iqGpKQRYqTpec/6PqJEQsi6zSfbuLG0+GMhAep7STIwS9rxh6OQfVk
Mg1c375VerioqCPJAgMBAAE=
-----END PUBLIC KEY-----
```

# Symmetric (AES) algorithm

## Instructions

AES content key should be provided in `data/aes-key.txt` file. It should have size of `8`, `16` or `32` `bytes`. For this example, the **content file** must have `128` `bytes`.

## AES Key Example

```aes
cRfUjXn2r5u8x/A?D(G+KbPeSgVkYp3s
```

# How to Use

Please install requirements on file `requirements.txt`. It can be installed using **Pip** for `Python 3`.

Please use a Python3 Interpreter and run `test.py` or any of the algorithm files.

Each algorithm file contains a main function, which consist on a test.

The result of test will generate a file named `./result.txt`.