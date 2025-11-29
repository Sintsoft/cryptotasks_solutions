import base64

class EncodingTools():

    def decodeHexFromstring(input_str: str) -> str:
        return bytes.fromhex(input_str).decode('utf-8')

    def decodeBase64HexString(input_str: str) -> str:
        return base64.b64encode(bytes.fromhex(input_str)).decode('utf-8')

    def decodeBase64String(input_str: str) -> str:
        return base64.b64decode(bytes(input_str, 'utf-8')).decode('utf-8')

    def decodeAsciiList(input_str: list) -> str:
        return "".join(chr(o) for o in input_str)

    def decodeHexInteger(input_str: str) -> str:
        return  bytearray.fromhex(input_str.split('x')[1]).decode('utf-8')



    def caesarRot(input_str: str, num: int) -> str:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        prep = input_str.strip()
        res = ''
        for ch in prep:
            res += alpha[(alpha.index(ch) + num) % len(alpha)] if ch != "_" else ch
        print(res)
        return res