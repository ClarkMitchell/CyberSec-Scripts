#!/usr/bin/env/ python
"""
SYNOPSIS

    script1.py will encode or decode to base64 which can be determined by the user.
    The script will prompt for a string to process and then return the originial and output.

AUTHOR

    Clark Mitchell

DATE

    September 26, 2014
"""

import sys, base64

def encode(string_to_encode):
    print(string_to_encode)
    print(base64.b64encode(string_to_encode))

def decode(string_to_decode):
    print(string_to_decode)
    print(base64.b64decode(string_to_decode))

def wants_to_encode():
    choice = raw_input('Encode, Decode or Quit: ')
    if choice in ['e', 'en', 'encode', 'Encode', 'ENCODE']:
        reply = 'e'
    elif choice in ['d', 'de', 'decode', 'Decode', 'DECODE']:
        reply = 'd'
    else:
        reply = 'q'
    return reply

def main():
    proceed = True
    while proceed:
         decision = wants_to_encode()
         if decision is 'e':
             string = raw_input("Enter a string to encode: ")
             encode(string)
         elif decision is 'd':
             string = raw_input("Enter a string to decode: ")
             decode(string)
         elif decision is 'q':
              print("Quitting... ")
              proceed = False
          
main()
        
