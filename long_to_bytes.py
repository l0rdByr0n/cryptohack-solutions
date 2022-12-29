from Crypto.Util.number import *

def bytes_convert(string):
    return long_to_bytes(string)

long = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

result = bytes_convert(long)
print(result)
