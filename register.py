import requests
import json
import sys

port = sys.argv[1]
url = 'http://127.0.0.1:'+port+'/register_with'
headers = {'Content-Type': 'application/json'}
data = {'node_address': 'http://127.0.0.1:8000'}
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)
