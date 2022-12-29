def xor(key1:str,key2:int)->bytes:
    return [a^b for a,b in zip(key1,key2)]


KEY1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
KEY2_1 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
KEY2_3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
FLAG_1_3_2 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')


KEY2 = xor(KEY1,KEY2_1)
KEY3 = xor(KEY2,KEY2_3)
KEY1_2_3 = xor(KEY3,KEY2_1)

flag = xor(KEY1_2_3,FLAG_1_3_2)
flag = "".join(chr(f) for f in flag)

print(flag)
