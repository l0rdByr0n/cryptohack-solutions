def xor(string: str,key: int):
    return "".join(chr(ord(a)^key) for a in string)

string = 'label'

result = xor(string,13)
print(result)
