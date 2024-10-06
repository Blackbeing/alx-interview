#!/usr/bin/python3
"""
Module to return minimum number of coins required.
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to make the
    specified total.
    Parameters:
        coins (list): A list of positive integers (coin denominations).
        total (int): Total amount to be achieved using the coin denominations.

    Returns:
        int: Minimum number of coins required to make up the total.
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    remaining_total = total

    for coin in coins:
        if remaining_total <= 0:
            break
        coin_count = remaining_total // coin
        num_coins += coin_count
        remaining_total -= coin * coin_count

    if remaining_total > 0:
        return -1

    return num_coins


if __name__ == "__main__":
    makeChange([1, 2, 25], 37)
