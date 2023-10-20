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
import logging
import random
import sys
import time

sys.path.append("..")

from blockchain.block import Block, gen_genesis
from util.simulation import miner_account, mining_time_list


class Blockchain:

    def __init__(self, target="0000"):
        self.chain = []
        self.chain.append(gen_genesis())
        self.target = target

    def length(self):
        return len(self.chain)

    def latest_block(self):
        return self.chain[-1]

    def set_target(self, target):
        self.target = target

    def mining(self, node_id):
        length = self.length()
        start_time = time.time()
        new_block = Block(self.latest_block().hash(), self.target, node_id)
        flag = False

        while True:
            # there is no new block
            if length == len(self.chain):
                nonce = str(random.randint(0, sys.maxsize))
                new_block.time_stamp = time.time()
                if new_block.check_nonce(nonce):
                    new_block.nonce = nonce
                    flag = True
                    break
            else:
                if self.latest_block().check():
                    break

        if flag:
            end_time = time.time()
            mining_time = end_time - start_time
            logging.info("One block is dug out. Its mining time is: %d. "
                         "Its miner is %d. " % (mining_time, node_id))
            mining_time_list.append(mining_time)
            if miner_account.get(node_id) is None:
                miner_account[node_id] = 1
            else:
                miner_account[node_id] = miner_account[node_id] + 1
            self.chain.append(new_block)

    def check(self):
        for i in range(1, self.length() - 1):
            if self.chain[i].check():
                continue
            else:
                print("WARNING: The block chain is NOT valid")
                return False
        print("The block chain is valid")
        return True

    def print(self):
        i = 1
        print("###########################################################")
        for b in self.chain:
            print("Block num %d" % i)
            i = i + 1
            b.display()
            print("###########################################################")


if __name__ == "__main__":
    chain = Blockchain()
    chain.mining(node_id=0)
    chain.print()
