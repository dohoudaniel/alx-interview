#!/usr/bin/python3
"""
Python Lockboxes
"""


def canUnlockAll(boxes):
    """
    Unlocking Lockboxes
    """
    total_boxes = len(boxes)
    setofkeys = [0]
    counter = 0
    index = 0
    while index < len(setofkeys):
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in setofkeys:
                setofkeys.append(key)
                counter += 1
        index += 1
    return counter == total_boxes - 1
