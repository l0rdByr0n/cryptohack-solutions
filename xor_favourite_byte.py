def syngle_byte_xor(text: bytes, key: int) -> bytes:
    return bytes([b ^ key for b in text])


cipher_hex = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
cipher = bytes.fromhex(cipher_hex)

for i in range(0,255):
    result = syngle_byte_xor(cipher,i).decode()
    if result[0] == 'c':
    	print(result)
    	break
