#!/usr/bin/python

import sys
sys.path.insert(1, 'Y:\\bin\\')
from ns_crypto.stenography import ImageSteganography

args = sys.argv
imgSrcPth = args[1]

try:
    tool = ImageSteganography(imgSrcPth)
    msg = tool.decode()
    print("Value:".format(msg))
except Exception as e:
    print(e)
