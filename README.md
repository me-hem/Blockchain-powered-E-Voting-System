# Blockchain-Powered E-Voting System

## Outline
1. Reference Repository
2. Modification in previously designed E-voting system
3. Instructions to run application
4. References

### Reference Repository
This project is based on the E-Voting system developed in (https://github.com/ramesh-adhikari/E-voting-system-using-blockchain-and-python) repository entitled "E-voting-system-using-blockchain-and-python" by Ramesh Adhikari.

**Appreciate the significant contributions made by the "E-voting-system-using-blockchain-and-python" repository in advancing my understanding and practical implementation of blockchain technology in the context of e-voting systems.**

This application aims to implement blockchain in an e-voting system, enabling voters to cast their votes using their unique voter IDs. The application ensures that each voter can only vote once, and the voted information is stored on the blockchain, making it immutable and permanent. Users interact with the application through a user-friendly web interface.

To achieve this, we follow a bottom-up approach, starting with defining the data structure for storing information in the blockchain. Each post in the blockchain consists of three essential elements: voter_id, party, and timestamp. We store this data in JSON format, and a sample post in the blockchain would include the voter ID, the political party chosen, and the timestamp of the vote.

``` "transactions": [
        {
          "voter_id": "VOID001",
          "party": "Democratic Party",
          "timestamp": 1649571086.02753
        }
      ],
```

To maintain the integrity of the data stored in the blockchain, we employ cryptographic hash functions. We compute the hash of each block, which acts as a digital fingerprint or signature of the data contained within it. This allows us to detect any tampering with the block's data.

``` def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
```

To create dependency among consecutive blocks and ensure the integrity of the entire chain, we chain the blocks together. Each block contains the hash of the previous block, creating a link between them. The first block in the chain, known as the genesis block, is either generated manually or through a unique logic.

``` class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
```

To further secure the blockchain, we implement the Proof of Work (PoW) algorithm. Miners compete to complete transactions and add new blocks to the chain. The algorithm makes the task of calculating the hash difficult and random by adding a constraint. Miners must find a nonce that satisfies the constraint, which serves as proof of the computation performed. The number of zeroes in the constraint determines the difficulty level of the PoW algorithm.

To add a block to the chain, we verify that the data is untampered and that the order of transactions is preserved. The Proof of Work provided must be correct, and the previous_hash field of the block to be added should point to the hash of the latest block in the chain.

![image.png](https://github.com/me-hem/E-voting-system-using-blockchain-and-python/blob/master/screenshots/5.png?raw=true)
*Figure 1: "Old system"*


Finally, we implement mining, which involves putting unconfirmed transactions into blocks and computing the Proof of Work. Once a nonce satisfying the constraint is found, a block is considered mined and can be added to the chain.

### Modification in previously designed E-voting system
There were several limitations in previously designed E-voting system such as:
- Manual Voting and Mining Process: Manual voting and mining processes can result in delays and inconsistencies in the voting and mining process, leading to significant differences in the number of transactions per block and overall mining time.
- Less Functionality in Web Page: The web page of the previous e-voting system lacked advanced functionality. Users had to click buttons to perform all actions, and there was no automatic syncing system.
- Insecure Voter Information: The previous e-voting system displayed voter identification and voting details in real-time, which compromised voter privacy. There was no mechanism to ensure the anonymity of voters.
- Lack of Mining Statistics: The previous e-voting system lacked mining statistics, leading to limited transparency and insights into its performance.

We overcame all these limitations by following modifications:
- Automated Voting and Mining Process: To overcome the limitations of the manual voting and mining process, we implemented two scripts, namely voting.py and mining.py. This automation process achieved better results and ensured timely mining and reduced the differences between the number of transactions in each block.
- Dynamic web page: We enhanced the functionality of the web page by making it dynamic, where the system syncs automatically every 5 seconds. This feature ensured that all the details, such as the mining statistics and leading party, were updated automatically.
- Voter Information Security: To enhance voter information security, we added a hashing feature that used SHA 256 to hash the voter IDs. This feature ensured that the voter's identity remained secure and confidential.
- Mining Statistics: Added mining statistics such as total voting time, total mining time, average mining time per block, average number of transactions per block, and the number of blocks mined.  These statistics get updated in real-time automatically, providing greater transparency and insight into the system's performance.

![image.png](https://github.com/me-hem/research_internship_work_BHU/blob/master/Voting%20system%20using%20Blockchain/Screenshots/mod_vote.png)
*Figure 2: "Modified System"*


### Instructions to run application
Clone the project,
```sh
$ git clone https://github.com/me-hem/blockchain_powered_e_voting_system
```
Install the dependencies,
```sh
$ cd blockchain_powered_e_voting_system
$ pip install -r requirements.txt
```
Start a blockchain node server,
```sh
# Windows users can follow this: https://flask.palletsprojects.com/en/1.1.x/cli/#application-discovery
$ export FLASK_APP=service.py
$ flask run --port 8000
```
One instance of our blockchain node is now up and running at port 8000.

Run the application on a different terminal session,
```sh
$ python3 app.py 5000
```
The application should be up and running at [http://localhost:5000](http://localhost:5000).

Now, run automation script simultaneously  i.e.

```sh
$ python3 voting.py 8000& python3 mining.py 8000&
```
Now, you can check mining performance and real-time voting results.

![image.png](https://github.com/me-hem/research_internship_work_BHU/blob/master/Voting%20system%20using%20Blockchain/Screenshots/flowchart.png)
*Figure 3: "Implementation of modified E-Voting system"*

### References
1. https://www2.deloitte.com/content/dam/Deloitte/uk/Documents/Innovation/deloitte-uk-what-is-blockchain-2016.pdf
2. https://doi.org/10.6028/NIST.IR.8202
3. https://github.com/me-hem/E-voting-system-using-blockchain-and-python
4. https://www.researchgate.net/publication/341498272_A_Conceptual_Secure_Blockchain_Based_Electronic_Voting_System
5. https://www.researchgate.net/publication/346463547_Understanding_Blockchain_Technology_and_how_to_get_involved
