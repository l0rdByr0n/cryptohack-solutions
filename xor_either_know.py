def xor(text : bytes, flag : str) -> bytes:
    return "".join([chr(a^ord(b)) for a,b in zip(text, flag)])

cipher_hex = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

cipher = bytes.fromhex(cipher_hex)

key = xor(cipher[:7],'crypto{')

print(key)

partial_key = "myXORkey"

key = partial_key*7
key = key[:42]

result = xor(cipher,key)
print(result)
