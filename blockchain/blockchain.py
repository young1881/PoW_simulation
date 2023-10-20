#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
----------------------------------------
# @File           :   blockchain.py    
# @Modify Time    :   2023-10-20 17:46
# @Author         :   young1881
# @Description    :   the class of blockchain
________________________________________
"""
import random
import sys

from blockchain.block import Block, gen_genesis


class Blockchain:

    def __init__(self, target="0000"):
        self.chain = list()
        self.chain = self.chain.append(gen_genesis())
        self.target = target

    def length(self):
        return self.chain.length()

    def latest_block(self):
        return self.chain[-1]

    def set_target(self, target):
        self.target = target

    def mining(self, node_id):
        length = len(self.chain)

        new_block = Block(self.latest_block().hash(), self.target, node_id)

        while True:
            # there is no new block
            if length == len(self.chain):
                nonce = str(random.randint(0, sys.maxsize))
                new_block.time_stamp = time.time()
                if new_block.check_nonce(nonce):
                    new_block.nonce = nonce
                    break
            else:
                if self.latest_block().check():
                    break
