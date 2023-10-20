#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
----------------------------------------
# @File           :   main.py
# @Modify Time    :   2023-10-20 18:18
# @Author         :   young1881
# @Description    :   simulation experiment
________________________________________
"""

import logging
import threading

from blockchain.blockchain import Blockchain
from util.simulation import get_evil_node_block

chain = Blockchain()
evil_chain = Blockchain()
hack_flag = False
max_trial = 5
miner_account = {}


def mining(node_id):
    logging.info("honest node %d is ready." % node_id)
    for j in range(0, max_trial):
        chain.mining(node_id)


def attacking(node_id):
    global hack_flag, chain
    logging.info("evil node %d is ready." % node_id)
    for j in range(0, max_trial):
        if hack_flag:
            chain.mining(node_id)
        else:
            evil_chain.mining(node_id)
            # other evil nodes haven't hacked the blockchain
            if evil_chain.length() > chain.length() and hack_flag is False:
                chain = evil_chain
                hack_flag = True
                logging.info("Attackers hack the chain at block num %d." % (evil_chain.length() - 1))
                logging.info("EVIL CHAIN WINS.")


def simulation(honest_node_num, evil_node_num, difficulty):
    nodes = []
    chain.set_target(difficulty)
    for i in range(1, honest_node_num):
        nodes.append(threading.Thread(target=mining, args=(i,)))
    for i in range(honest_node_num, honest_node_num + evil_node_num):
        nodes.append(threading.Thread(target=attacking, args=(i,)))

    i = 1
    # start honest nodes
    for n in nodes:
        n.start()
        logging.info("node %d starts mining." % (i + 1))
        i = i + 1

    for n in nodes:
        n.join()

    if chain.check():
        chain.print()
        logging.info("block chain length is: %d", chain.length())
        logging.info("total evil blocks is: %d" % get_evil_node_block(honest_node_num))

    else:
        logging.warning("THE BLOCK CHAIN IS NOT VALID.")


if __name__ == '__main__':
    simulation(honest_node_num=3, evil_node_num=0, difficulty="0000")

