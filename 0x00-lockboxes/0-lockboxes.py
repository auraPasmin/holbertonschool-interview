#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """ Coment """
    box = len(boxes) * [False]
    box[0] = True
    keys = [0]

    for each in keys:
        for i in boxes[each]:
            if i not in keys:
                if i < len(boxes):
                    box[i] = True
                    keys.append(i)
    return all(box)
