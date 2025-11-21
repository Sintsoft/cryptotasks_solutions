import base64

class EncodingTools():

    def decodeHexFromstring(input: str) -> str:
        return str(bytes.fromhex(input))

    def decodeBase64String(input: str) -> str:
        return base64.b64encode(bytes.fromhex(input)).decode('utf-8')

    def decodeAsciiList(input: list) -> str:
        return "".join(chr(o) for o in input)