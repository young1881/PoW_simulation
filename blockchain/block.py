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

    def __init__(self, pre_hash, target="0000", node_id=-1):
        self.pre_hash = pre_hash
        self.nonce = str(random.randint(0, sys.maxsize))
        self.time_stamp = time.time()
        self.target = target
        self.node_id = node_id

    def hash(self):
        """
        :return: the hash value of blockchain
        """
        s = sha256()
        s.update(self.pre_hash.encode("utf-8"))
        s.update(self.nonce.encode("utf-8"))
        s.update(str(self.time_stamp).encode("utf-8"))
        hash_value = s.hexdigest()
        return hash_value

    def check(self):
        return self.check_nonce(self.nonce)

    def check_nonce(self, nonce):
        """
        :param nonce: the trial nonce while mining
        :return: true if none hash_value less than target
        """
        s = sha256()
        s.update(self.pre_hash.encode("utf-8"))
        s.update(self.nonce.encode("utf-8"))
        s.update(str(self.time_stamp).encode("utf-8"))
        hash_value = s.hexdigest()
        return hash_value.startswith(self.target)

    def set_genesis(self):
        """
        set the block to be genesis
        """
        self.nonce = str(0)
        self.time_stamp = 0
        self.pre_hash = str(0)


def gen_genesis():
    genesis = Block(pre_hash=str(0))
    genesis.set_genesis()
