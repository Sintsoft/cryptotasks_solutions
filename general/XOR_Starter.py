from pwn import *

word = b"label"

print(xor(word, 13))