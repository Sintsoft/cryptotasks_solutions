'''
Now you've got the hang of the various encodings you'll be encountering, let's have a look at automating it.

Can you pass all 100 levels to get the flag?

The 13377.py file attached below is the source code for what's running on the server. The pwntools_example.py file provides the start of a solution.

For more information about connecting to interactive challenges, see the FAQ. Feel free to skip ahead to the cryptography if you aren't in the mood for a coding challenge!

If you want to run and test the challenge locally, then check the FAQ to download the utils.listener module.

Connect at socket.cryptohack.org 13377
'''
import base64
from pwn import * # pip install pwntools
import json

import tools.encoding_tools as ec


ENCODINGS = [
    "base64",
    "hex",
    "rot13",
    "bigint",
    "utf-8",
]

def decodeme(message):
    output = ""
    if message["type"] == "utf-8":
        output = ec.EncodingTools.decodeAsciiList(message["encoded"])
        print("output = " + output)
    elif message["type"] == "base64":
        output = ec.EncodingTools.decodeBase64String(message["encoded"])
        print("output = " + str(output))
    elif message["type"] == "bigint":
        output = ec.EncodingTools.decodeHexInteger(message["encoded"])
        print("output = " + output)
    elif message["type"] == "hex":
        output = ec.EncodingTools.decodeHexFromstring(message["encoded"])
        print("output = " + str(output))
    elif message["type"] == "rot13":
        output = ec.EncodingTools.caesarRot(message["encoded"], 13)
        print("output = " + str(output))
    else:
        print(message["type"])
    return str(output)





def start():
    r = remote('socket.cryptohack.org', 13377, level='debug')

    def json_recv():
        line = r.recvline()
        return json.loads(line.decode())

    def json_send(hsh):
        request = json.dumps(hsh).encode()
        r.sendline(request)

    received = json_recv()

    while True:

        if received.keys().__contains__("flag"):
            print(received)
            break

        if received.keys().__contains__("error"):
            print(received)
            break

        print("Received type: ")
        print(received["type"])
        print("Received encoded value: ")
        print(received["encoded"])

        to_send = {
            "decoded": decodeme(received)
        }
        json_send(to_send)

        received = json_recv()


if __name__ == '__main__':
    start()
    #print(base64.b64decode("YXBwX3JlcHJlc2VudGF0aXZlc19naGFuYQ=="))
    #print(ec.EncodingTools.decodeHexFromstring("636f6e735f64697374616e6365735f736563"))

