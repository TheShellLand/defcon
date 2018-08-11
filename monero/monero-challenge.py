import hashlib
import binascii
import pandas as pd
import string
import base64
import codecs

from Crypto.Cipher import AES


def string_to_char(input):
    """Turn hexstring to ASCII"""
    length = len(input)

    c = []

    i = 0
    while i < length:
        chars = chr(int(input[i:i + 2], 16))
        c.append(chars)
        i += 2

    final = ''.join(c)
    return final


def ascii_only(input):
    """Return only if the input is an ASCII character"""
    if input in string.ascii_letters:
        return input


def decrypt_aes(encrypted, key):
    """Decrypt a bytestring using AES"""
    pass


def ascii_to_bin(input):
    """Turn a hexstring into a bytestring"""
    length = len(input)

    c = []

    i = 0
    while i < length:
        chars = chr(int(input[i:i + 2], 16)).encode()
        c.append(chars)
        i += 2

    final = b''.join(c)
    return final


def rot13(input):
    s = input
    enc = codecs.getencoder("rot-13")
    os = enc(s)[0]

    return os


# Message in the front of the coin
# rot 13
# Decrypted message is: crypto means crypto mea
front = '70 65 6c 63 67 62 20 7a 72 6e 61 ' \
        '66 20 70 65 6c 63 67 62 20 7a 72 ' \
        '6e'
front = front.split()
front = ''.join(front)
df = pd.Series(front)
key = df.apply(string_to_char)
key = key.to_frame()
key = key.to_records()
key = key[0][1]
key = rot13(key)
print(key)

# Message on the back of the coin
# no idea what this decrypts into yet
# TODO: try AES
back = '28 00 00 00 00 00 0c 4d 36 14 1e ' \
       '16 52 0e 13 17 57 07 4f 50 08 11 ' \
       '41 0a 1c 47 43 1b 17 50 00 07 45 ' \
       '4d 15 0e 1e 06 0f 13 0b 50 17 00 ' \
       '4d 04 06 4d 4e 10 41 11 06 16 1f ' \
       '1a 43 00 0c 0b 05 4e 1e 4f 15 1b ' \
       '1c 50 07 0a 52 04 00 12'
back = back.split()
back = ''.join(back)
df = pd.Series(back)
back_encrypted = df.apply(ascii_to_bin)
back_encrypted = back_encrypted.to_frame()
back_encrypted = back_encrypted.to_records()
back_encrypted = back_encrypted[0][1]
print(back_encrypted)
# write out the hexbytes conversion to a file
with open('back.enc', 'wb') as f:
    f.write(back_encrypted)

pass
