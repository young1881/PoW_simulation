#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
----------------------------------------
# @File           :   simulation.py    
# @Modify Time    :   2023-10-20 21:40
# @Author         :   young1881
# @Description    :   
________________________________________
"""

mining_time_list = []
miner_account = {}


def get_evil_node_block(honest_node_num):
    evil_miner_blocks = []
    for miner in miner_account:
        if miner > honest_node_num:
            evil_miner_blocks.append(miner_account[miner])
    total_evil_blocks = 0
    for b in evil_miner_blocks:
        total_evil_blocks = total_evil_blocks + b
    return total_evil_blocks
