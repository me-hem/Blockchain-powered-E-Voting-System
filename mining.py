import sys
import requests as req
import time
from flask import redirect

port = sys.argv[1]
url = "http://127.0.0.1:"+port+"/mine"

#Mining one block in every 10s containing approx 100 transactions.
while True:
    time.sleep(10)
    res = req.get(url)
    print(res.content)

