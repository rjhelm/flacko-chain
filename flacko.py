import hashlib
from re import I
from time import time
from pprint import pprint

class flackochain():
    def __init__(self):
        self.blocks = []
        self.__secret = ''
        self.__difficulty = 4
        # guessing the nonce
        secret_string = '/*SECRET*/'
        while True:
            _hash = hashlib.sha256(str(secret_string+str(i)).oncode('utf-8')).hexdigest()
            if(_hash[:self.__difficulty] == '0' * self.__difficulty):
                self.__secret = _hash
                break
            i += 1
    
    def create_block(self, sender:str, information:str):
        block = {
            'index': len(self.blocks),
            'sender': sender,
            'timestanp': time(),
            'info': information
        } 
        # For genesis block
        if(block['index'] == 0): block['previous_hash'] = self.__secret
        else: block['previous_hash'] = self.blocks[-1]['hash']
        # guessing the nonce
        i = 0
        while True:
            block['nonce'] = i
            _hash = hashlib.sha256(str(block).encode('utf-8')).hexdigest()
            if(_hash[:self.__difficulty] == '0' * self.__difficulty):
                block['hash'] = _hash
                break
            i += 1
        self.blocks.append(block)
        
    def validate_blockchain(self):
        