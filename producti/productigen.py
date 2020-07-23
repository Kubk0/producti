import base64 
import os 
import fileinput
import secrets
import time
import random
import string
f = open("productkeysgenerated.txt", "a")
def get_random_string():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(13))
    gen = result_str
    print(gen)
    message = "pdk" + gen
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    f.write(base64_message + "\n")
a = 60
while a > 0:
    get_random_string()
    a-=1
    print(a)
    time.sleep(1)
    get_random_string()
   

f.close()



