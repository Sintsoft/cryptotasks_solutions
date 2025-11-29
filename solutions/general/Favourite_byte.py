
from pwn import *
from tools.encoding_tools import EncodingTools as et

if __name__ == '__main__':
    input_str = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

    b = 1
    num = int(input_str, 16)
    while b < num:

        print(xor(bytes.fromhex(input_str), b))
        b *= 2


