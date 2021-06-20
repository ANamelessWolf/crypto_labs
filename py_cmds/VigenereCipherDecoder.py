#!/usr/bin/python

import sys
sys.path.insert(1, 'Y:\\bin\\')
from ns_crypto.VigenereCipher import VigenereCipher

args = sys.argv
key = args[1]
msg = args[2]

try:
    tool = VigenereCipher(key)
    decodeMsg = tool.decode(msg)
    msgAsString = "\n".join(list(map(lambda x: str(x), decodeMsg)))
    print("{0}".format(msgAsString))
except Exception as e:
    print(e)
