import sys
import requests as req
import time

port = sys.argv[1]
url = "http://127.0.0.1:" + port + "/mine"

print("Mining started ")
count = 0
while count < 3:
    time.sleep(10)
    res = req.get(url)
    print(res.content.decode('utf-8'))
    if res.content.decode('utf-8') == "No transactions to mine":
        count += 1

print("Mining completed successfully")
