# This the automation file for voting process
import sys
import requests as req
import time
import random
from hashlib import sha256 

port = sys.argv[1]
url = "http://127.0.0.1:"+port+"/new_transaction"

Voter_Id = ["VOID"+(5 - len(str(i)))*"0"+str(i) for i in range(1,10001)]
Political_Parties = ["Democratic Party","Republican Party","Socialist party"]

def gen_hash(vid):
    return sha256(vid.encode()).hexdigest()

def get_vote():
    hashed_vid = gen_hash(Voter_Id.pop(random.randint(0, len(Voter_Id)-1)))
    party =  Political_Parties[random.randint(0, 2)]
    return hashed_vid, party

while len(Voter_Id):
    data = get_vote()
    post_object = {
        'voter_id': data[0],
        'party': data[1]
    }
    
    req.post(url, json=post_object, headers={'Content-type':'application/json'})
    time.sleep(0.1)

print("Voting completed successfully...")