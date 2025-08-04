# Blockchain-Powered E-Voting System

A secure, transparent, and tamper-proof electronic voting system built using blockchain technology and Python. This system ensures voter anonymity, prevents double voting, and provides immutable vote records through a decentralized blockchain implementation.

## Features

- **Blockchain Security**: Immutable vote storage using SHA-256 hashing and Proof of Work consensus
- **Voter Privacy**: Anonymized voter IDs using cryptographic hashing
- **Automated Processing**: Automated voting and mining scripts for efficient operation
- **Real-time Monitoring**: Dynamic web interface with live updates every 5 seconds
- **Mining Statistics**: Comprehensive performance metrics and transparency features
- **Tamper-Proof**: Cryptographic verification ensures data integrity
- **Decentralized**: Supports multiple blockchain nodes for distributed operation

## System Architecture

The system follows a bottom-up blockchain architecture with the following components:

### Data Structure
Each vote is stored as a transaction in the blockchain with:
```json
{
  "voter_id": "hashed_voter_id",
  "party": "Selected Political Party", 
  "timestamp": 1649571086
}
```

### Core Components
- **Block**: Contains index, transactions, timestamp, previous hash, and nonce
- **Blockchain**: Manages the chain of blocks with Proof of Work validation
- **Mining**: Automated process for adding verified transactions to blocks
- **Web Interface**: Flask-based frontend for interaction and monitoring

## Prerequisites

- Python 3.7 or higher
- pip package manager
- Git

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/me-hem/blockchain_powered_e_voting_system
cd blockchain_powered_e_voting_system
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the Blockchain Node
```bash
# For Unix/Linux/Mac
export FLASK_APP=service.py
flask run --port 8000

# For Windows
set FLASK_APP=service.py
flask run --port 8000
```

### 4. Launch the Web Application
Open a new terminal and run:
```bash
python3 app.py 5000
```

The application will be available at [http://localhost:5000](http://localhost:5000)

### 5. Start Automated Voting and Mining
In another terminal, run:
```bash
python3 voting.py 8000 & python3 mining.py 8000 &
```

## Usage

### Manual Voting
1. Access the web interface at `http://localhost:5000`
2. Submit votes through the user interface
3. Monitor real-time voting statistics and results

### Automated Simulation
The system includes automation scripts that simulate:
- **voting.py**: Generates 10,000 randomized votes with hashed voter IDs
- **mining.py**: Continuously mines pending transactions into blocks

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/new_transaction` | POST | Submit a new vote transaction |
| `/chain` | GET | Retrieve the complete blockchain |
| `/mine` | GET | Mine pending transactions |
| `/pending_tx` | GET | View unconfirmed transactions |
| `/register_node` | POST | Add new peer nodes |


## System Improvements

This enhanced version addresses several limitations of the original system:

###  What's New
- **Automated Operations**: Eliminated manual voting/mining bottlenecks
- **Enhanced Security**: SHA-256 hashing for voter ID anonymization
- **Real-time Updates**: Dynamic web interface with automatic synchronization  
- **Performance Metrics**: Comprehensive mining and voting statistics

### Performance Statistics
The system tracks and displays:
- Total voting time
- Total mining time  
- Average mining time per block
- Average transactions per block
- Number of blocks mined
- Leading party in real-time

## System Flow

```
Voter Registration → Vote Submission → Transaction Pool → 
Mining Process → Block Creation → Chain Validation → 
Result Tabulation → Real-time Display
```

## Security Features

- **Cryptographic Hashing**: SHA-256 for block integrity and voter anonymization
- **Proof of Work**: Prevents malicious block creation
- **Chain Validation**: Ensures blockchain integrity across the network
- **Immutable Records**: Once recorded, votes cannot be altered or deleted
- **Decentralized Consensus**: Multiple nodes validate transactions

## Technical Stack

- **Backend**: Python 3.7+, Flask
- **Blockchain**: Custom implementation with SHA-256 and PoW
- **Frontend**: HTML, CSS, JavaScript
- **Networking**: HTTP/JSON API communication
- **Cryptography**: hashlib (SHA-256)

## Acknowledgments

This project builds upon the foundational work from the [E-voting-system-using-blockchain-and-python](https://github.com/ramesh-adhikari/E-voting-system-using-blockchain-and-python) repository by Ramesh Adhikari. We appreciate the significant contributions that advanced our understanding of blockchain technology in e-voting systems.

## References

1. [Deloitte - What is Blockchain?](https://www2.deloitte.com/content/dam/Deloitte/uk/Documents/Innovation/deloitte-uk-what-is-blockchain-2016.pdf)
2. [NIST Blockchain Technology Overview](https://doi.org/10.6028/NIST.IR.8202)
3. [A Conceptual Secure Blockchain Based Electronic Voting System](https://www.researchgate.net/publication/341498272_A_Conceptual_Secure_Blockchain_Based_Electronic_Voting_System)
4. [Understanding Blockchain Technology](https://www.researchgate.net/publication/346463547_Understanding_Blockchain_Technology_and_how_to_get_involved)

---
