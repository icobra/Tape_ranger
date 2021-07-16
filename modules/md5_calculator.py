#!/usr/bin/python3
#This module calculate MD5 checksum of file and return his sum.
from hashlib import md5 as md5

# Warning! The file is read in blocks specified in the BLOCKS variable.
BLOCKS = 268435456 # Buffer size in bytes.

wordlistfile = open("test","rb")
world_string = wordlistfile.read()


answer = md5(world_string).hexdigest()
print(answer)

wordlistfile = open("test2","r",encoding='utf-8')
world_string = wordlistfile.read()


answer = md5(world_string.encode('utf-8')).hexdigest()
print(answer)