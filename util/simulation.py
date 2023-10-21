#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
----------------------------------------
# @File           :   simulation.py    
# @Modify Time    :   2023-10-20 21:40
# @Author         :   young1881
# @Description    :   mining related experimental utils
________________________________________
"""
import logging
import sys

mining_time_list = []
miner_account = {}


def get_evil_node_block(honest_node_num):
    total_evil_blocks = sum(miner_account[miner] for miner in miner_account if miner > honest_node_num)
    return total_evil_blocks


def get_growth_rate():
    if not mining_time_list:
        return None

    total_mining_time = 0
    max_mining_time = -1
    min_mining_time = sys.maxsize

    for m in mining_time_list:
        total_mining_time += m
        if m > max_mining_time:
            max_mining_time = m
        if m < min_mining_time:
            min_mining_time = m

    if len(mining_time_list) > 1:
        average_mining_time = total_mining_time / (len(mining_time_list) - 1)
    else:
        average_mining_time = 0

    logging.info("Average Mining Time is: %f" % average_mining_time)
    logging.info("Maximum Mining Time is: %f" % max_mining_time)
    logging.info("Minimum Mining Time is: %f" % min_mining_time)


def get_benefit(honest_node_num, evil_node_num, difficulty):
    evil_block = 0
    for i in range(honest_node_num + 1, honest_node_num + evil_node_num + 1):
        if i in miner_account:
            evil_block += miner_account[i]
    total_block = evil_block
    for i in range(1, honest_node_num + 1):
        if i in miner_account:
            total_block += miner_account[i]
    benefit_ratio = 100 * evil_block / total_block
    evil_ratio = 100 * evil_node_num / (honest_node_num + evil_node_num)
    logging.info("Benefit Ratio is %.1f%% when %.1f%% of nodes are evil and difficulty is %s",
                 benefit_ratio, evil_ratio, difficulty)
