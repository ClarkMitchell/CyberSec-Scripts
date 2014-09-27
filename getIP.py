#!/usr/bin/env python
"""
DESCRIPTION

    This script scrapes the html index of the provided url,
    iterates through the html to find domains and then
    creates an output text file of unique links and their
    associated IP addresses.

AUTHOR

    Clark Mitchell

"""

import socket
import sys
import urllib2
import string

def main ():

    working_file = set()
    url = raw_input("URL: ")
    html = urllib2.urlopen(url)
    
    for line in html:
        if 'href' in line:
            current = line[line.find("//") + 2 :]
            new_current = current[:current.find('/')]
            if '<' not in new_current:
                working_file.add(new_current + '\n')

    working_file = list(working_file)            
    working_file.sort()
    unique_link = set()
    output_file = open("output.txt", "w+")
	
    for line in working_file:
        if line not in unique_link:
            output_file.write(line)
	    output_file.write(socket.gethostbyname(line.replace("\n", "")) + "\n\n")
            unique_link.add(line)
            

main()

