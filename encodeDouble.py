#!/usr/bin/env/ python
"""
SYNOPSIS

    encodeDouble.py will encode or decode to base64, encode to md5, and encode first to base64
    and then md5. The script will prompt for a string to process and then return the originial
    and output.

AUTHOR

    Clark Mitchell

DATE

    September 27, 2014
"""

import sys, base64, hashlib

def encode_base64(string_to_encode):
    print(string_to_encode)
    print(base64.b64encode(string_to_encode))

def encode_md5(string_to_encode):
    print(string_to_encode)
    md = hashlib.md5(string_to_encode).hexdigest()
    print(md)

def encode_both(string_to_encode):
    print(string_to_encode)
    base = (base64.b64encode(string_to_encode))
    both = hashlib.md5(base).hexdigest()
    print(both)
    
def decode(string_to_decode):
    print(string_to_decode)
    length = len(string_to_decode)
    remainder = length % 4
    if remainder is not 0:
	print("The string provided was not base64")
    else:
        print(base64.b64decode(string_to_decode))

def wants_to_encode():
    choice = raw_input('Encode, Decode or Quit: ')
    if choice in ['e', 'en', 'encode', 'Encode', 'ENCODE']:
        reply = determine_encoding()
    elif choice in ['d', 'de', 'decode', 'Decode', 'DECODE']:
        reply = 'd'
    else:
        reply = 'q'
    return reply

def determine_encoding():
    choice2 = raw_input('Base64, MD5, or both? ')
    if choice2 in ['base64', 'base', 'Base64', 'BASE', 'BASE64']:
        reply2 = '64'
    elif choice2 in ['m', 'md', 'md5', 'MD5']:
        reply2 = 'md5'
    elif choice2 in ['b', 'both', 'Both', 'BOTH']:
        reply2 = 'b'
    else:
        reply2 = -1
    return reply2

def main():
    proceed = True
    while proceed:
         decision = wants_to_encode()
         if decision is '64':
             string = raw_input("Enter a string to encode in base64: ")
             encode_base64(string)
         elif decision is 'md5':
             string = raw_input("Enter a string to encode in md5: ")
             encode_md5(string)
         elif decision is 'b':
             string = raw_input("Enter a string to encode (base64 to md5): ")
             encode_both(string)
         elif decision is 'd':
             string = raw_input("Enter a string to decode: ")
             decode(string)
         elif decision is 'q':
              print("Quitting... ")
              proceed = False
         else:
             sys.exit()
          
main()
        
