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
from util.simulation import get_evil_node_block, get_growth_rate, get_benefit
from util.log import init_log

chain = Blockchain()
evil_chain = Blockchain()
hack_flag = False
max_trial = 10
miner_account = {}


def mining(node_id):
    logging.info("Honest Node %d is ready." % node_id)
    for j in range(0, max_trial):
        chain.mining(node_id)


def attacking(node_id):
    global hack_flag, chain
    logging.info("Evil Node %d is ready." % node_id)
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
    init_log(honest_node_num, evil_node_num, difficulty)

    nodes = []
    chain.set_target(difficulty)
    evil_chain.set_target(difficulty)
    for i in range(1, honest_node_num+1):
        nodes.append(threading.Thread(target=mining, args=[i]))
    for i in range(honest_node_num+1, honest_node_num + evil_node_num+1):
        nodes.append(threading.Thread(target=attacking, args=[i]))

    i = 1

    for n in nodes:
        n.start()
        logging.info("Node %d starts mining." % i)
        i = i + 1

    for n in nodes:
        n.join()

    if chain.check():
        chain.print()

        logging.info("__________________________________")
        logging.info("Current length is: %d", chain.length())
        logging.info("Total Evil Blocks are: %d" % get_evil_node_block(honest_node_num))
        get_growth_rate()
        get_benefit(honest_node_num, evil_node_num, difficulty)
        logging.info("__________________________________")

    else:
        logging.warning("THE BLOCK CHAIN IS NOT VALID.")

    exit()


if __name__ == '__main__':
    simulation(honest_node_num=9, evil_node_num=1, difficulty="00000")

