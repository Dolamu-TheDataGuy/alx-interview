#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet a given total
    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met
    Return:
        Number of coins or -1 if meeting the total is not possible
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total % coin == 0:
            coin_count += int(total / coin)
            return coin_count
        if total - coin >= 0:
            if int(total / coin) > 1:
                coin_count += int(total / coin)
                total = total % coin
            else:
                coin_count += 1
                total -= coin
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_count

