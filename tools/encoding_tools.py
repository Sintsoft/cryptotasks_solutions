import base64

class EncodingTools():

    def decodeHexFromstring(input: str) -> str:
        return bytes.fromhex(input).decode('utf-8')

    def decodeBase64HexString(input: str) -> str:
        return base64.b64encode(bytes.fromhex(input)).decode('utf-8')

    def decodeBase64String(input: str) -> str:
        return base64.b64decode(bytes(input, 'utf-8')).decode('utf-8')

    def decodeAsciiList(input: list) -> str:
        return "".join(chr(o) for o in input)

    def decodeHexInteger(input: str) -> str:
        return  bytearray.fromhex(input.split('x')[1]).decode('utf-8')



    def caesarRot(input: str, num: int) -> str:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        prep = input.strip()
        res = ''
        for ch in prep:
            res += alpha[(alpha.index(ch) + num) % len(alpha)] if ch != "_" else ch
        print(res)
        return res