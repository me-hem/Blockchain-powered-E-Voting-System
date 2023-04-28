import datetime
import json

import requests
from flask import render_template, redirect, request
from flask import flash
from app import app

import time

# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_SERVICE_ADDRESS = "http://127.0.0.1:8000"
POLITICAL_PARTIES = ["Democratic Party","Republican Party","Socialist party"]

vote_check=[]

posts = []

current_time = time.time()

def fetch_posts():
    """
    Function to fetch the chain from a blockchain node, parse the
    data and store it locally.
    """
    get_chain_address = "{}/chain".format(CONNECTED_SERVICE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        vote_count = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)


        global posts
        posts = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)

@app.route('/')
def index():
    fetch_posts()
    get_chain_address = "{}/chain".format(CONNECTED_SERVICE_ADDRESS)
    response = requests.get(get_chain_address)

    # retrieving chain length for calculating total number of blocks
    chain_length = response.json()["length"]
    
    # calculating time difference to calculate voting time
    if chain_length > 1:
        time_diff= datetime.datetime.fromtimestamp(response.json()["chain"][-1]["timestamp"]) - datetime.datetime.fromtimestamp(response.json()["chain"][1]["transactions"][0]["timestamp"])#datetime.datetime.fromtimestamp(current_time)
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        Voting_Time = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
            
    else:
        Voting_Time = "00:00:00"
    
    
    # calculating total mining time
    if chain_length > 1:
        temp_time = time_diff.seconds - (chain_length-1)*10
        mining_time = round(temp_time,4)
        # calculating average mining time
        average_time = round(temp_time/(chain_length-1),4)
    else:
        mining_time, average_time = 0, 0

    
    # comparing no. of votes of each party to decide leading party
    vote_gain = []
    for post in posts:
        vote_gain.append(post["party"])

    
    max_vote, total_votes = float('-inf'), 0

    for p in POLITICAL_PARTIES:
        if vote_gain.count(p) > max_vote:
            leading_party = p
            max_vote = vote_gain.count(p)
        total_votes += vote_gain.count(p)
    if chain_length == 1:
        leading_party = "-------"
    
    
     # calculating average number of transactions per block
    average_transaction = 0
    if chain_length > 1:
        average_transaction = total_votes//(chain_length-1)


    return render_template('index.html',
                           title='Blockchain-Powered E-Voting System',
                           posts=posts,
                           vote_gain=vote_gain,
                           node_address=CONNECTED_SERVICE_ADDRESS,
                           readable_time=timestamp_to_string,
                           political_parties = POLITICAL_PARTIES,
                           voting_time = Voting_Time,
                           length = chain_length,
                           average_time = average_time,
                           leading_party = leading_party,
                           mining_time = mining_time,
                           average_transaction = average_transaction)



def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M')
