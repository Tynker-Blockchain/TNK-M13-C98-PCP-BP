from web3 import Web3
import time
from datetime import datetime

ganacheUrl = "http://127.0.0.1:7545" 
web3 = Web3(Web3.HTTPProvider(ganacheUrl))

class Account():
    def __init__(self):
        self.account = web3.eth.account.create()
        self.address = self.account.address
        self.privateKey = self.account.key.hex()

class Wallet():
    def __init__(self):
        self.transactions = {}

    def checkConnection(self):
        if web3.is_connected():
           return True
        else:
            return False
        
    def makeTransactions(self, senderAddress, receiverAddress, amount, senderType, privateKey = None):
        web3.eth.defaultAccount = senderAddress
        if(senderType == 'ganache'):
            tnxHash = web3.eth.send_transaction({
                "from": senderAddress,
                "to": receiverAddress,
                "value": web3.to_wei(amount, "ether")  
                })  
        else:
            transaction = {
                "to": receiverAddress,
                "value": web3.to_wei(amount, "ether"),
                "nonce": web3.eth.get_transaction_count(senderAddress), 
                "gasPrice": web3.to_wei(10, 'gwei'),
                "gas": 21000 
            }
            signedTx = web3.eth.account.sign_transaction(transaction, privateKey)
            tnxHash = web3.eth.send_raw_transaction(signedTx.rawTransaction)
    
        return tnxHash.hex()
        
    def getBalance(self, address):
        balance = web3.eth.get_balance(address)
        return web3.from_wei(balance, 'ether')
    
    def addTransactionHash(self, tnxHash, senderAddress, receiverAddress, amount):
        self.transactions[tnxHash] = {
            "from":senderAddress,
            "to":receiverAddress,
            "tnxHash":tnxHash,
            "amount":amount,
            "time": time.time()
            }
        
     # Define getTransactions() method with address parameter
     
        # Create useTransactions as empty list
        
        # Loop through each tnxHash in self.transactions
        
            # Check if "from and "to" address matches with the address variable
            
                # Append the transaction to userTransactions list
                
                # Check if type of userTransactions[-1]['time'] is int
                
                    # Change the time to readable format
                    
                    
        # Sort the list of transactions based on the 'time' property

        # Return transactions