from pwn import * # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

i = 0
while i < 100:
	
	received = json_recv()
	print("Received type: ")
	print(received["type"])
	print("Received encoded value: ")
	print(received["encoded"])

	if received["type"] == 'base64':
		to_send = {
    			"decoded": base64.b64decode(received["encoded"].encode()).decode()
		}
	elif received["type"] == "bigint":
		received = int(received["encoded"], base=16)
		to_send = {
			"decoded": 	long_to_bytes(received).decode()
		}
	elif received["type"] == "hex":
		to_send = {
			"decoded": bytes.fromhex(received["encoded"]).decode()
			}
	elif received["type"] == "rot13":
		to_send = {
			"decoded": codecs.decode(received["encoded"],'rot13')
			}
	elif received["type"] == 'utf-8':
		to_send = {
			"decoded": "".join([chr(b) for b in received["encoded"]])
			}

	json_send(to_send)

	
	i += 1
	
print(json_recv())
