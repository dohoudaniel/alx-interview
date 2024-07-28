#!/usr/bin/python3
"""
The 0x08 Making Change project
"""


def makeChange(coins, total):
    """
    Add missing documentation
    """
    if total <= 0:
        return 0
    # sort the coins in descending order
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
