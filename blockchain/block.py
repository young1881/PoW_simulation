#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
----------------------------------------
# @File           :   block.py    
# @Modify Time    :   2023-10-20 17:38
# @Author         :   young1881
# @Description    :   class of block
________________________________________
"""

import random
import sys
import time
from hashlib import sha256


class Block:

    def __init__(self, pre_hash, target="000", node_id=-1):
        self.pre_hash = pre_hash
        self.nonce = str(random.randint(0, sys.maxsize))
        self.time_stamp = time.time()
        self.target = target
        self.node_id = node_id

    def hash(self):
        """
        :return: the hash value of blockchain
        """
        sh = sha256()
        sh.update(self.pre_hash.encode("utf-8"))
        sh.update(self.nonce.encode("utf-8"))
        sh.update(str(self.time_stamp).encode("utf-8"))
        hash_value = sh.hexdigest()
        return hash_value

    def check(self):
        return self.check_nonce(self.nonce)

    def check_nonce(self, nonce):
        """
        :param nonce: the trial nonce while mining
        :return: true if none hash_value less than target
        """
        sh = sha256()
        sh.update(self.pre_hash.encode("utf-8"))
        sh.update(nonce.encode("utf-8"))
        sh.update(str(self.time_stamp).encode("utf-8"))
        hash_value = sh.hexdigest()
        return hash_value.startswith(self.target)

    def set_genesis(self):
        """
        set the block to be genesis
        """
        self.nonce = str(0)
        self.time_stamp = time.time()
        self.pre_hash = str(0)

    def display(self):
        print("previous hash is:", self.pre_hash)
        print("nonce is:", self.nonce)
        print("time stamp is:", self.time_stamp)
        print("difficulty is:", self.target)
        print("hash value is:", self.hash())


def gen_genesis():
    genesis = Block(pre_hash=str(0))
    genesis.set_genesis()
    return genesis


if __name__ == "__main__":
    s = sha256()
    s.update("hello world".encode("utf-8"))
    initial_hash = s.hexdigest()
    new_block = Block(initial_hash)
    new_block.display()