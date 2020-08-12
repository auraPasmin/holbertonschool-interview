#!/usr/bin/python3
"""
Script function minOperations(n)
"""


def minOperations(n):
    """
    Function
    """
    num = n
    div = 2
    cont = 0

    if num <= 1:
        return 0

    while num > 1:
        if num % div == 0:
            num = int(num/div)
            cont += div
        else:
            div += 1
    return cont
