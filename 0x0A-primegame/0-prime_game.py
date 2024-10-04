#!/usr/bin/python3
"""
This module contains a function that determines the winner of a game played.
"""


def is_prime_sieve(max_n):
    """Generate a list to determine prime status of numbers up to `max_n` using
    the Sieve of Eratosthenes."""
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for start in range(2, int(max_n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_n + 1, start):
                sieve[multiple] = False
    return sieve


def isWinner(x, nums):
    """
    The `isWinner` function determines the winner of a game played by two
    players. The game consists of multiple rounds, each
    involving the calculation of the number of prime numbers up to a given
    integer specified by the list `nums`. It utilizes the Sieve of
    Eratosthenes, via the `is_prime_sieve` function, to efficiently determine
    prime numbers.

    Functionality:
    - Handles initial parameter validation, checking for a non-positive number
      of rounds (`x`) or an empty `nums` list.
    - Uses `is_prime_sieve` to create a Boolean array indicating the primality
      of numbers up to the maximum number present in `nums`.
    - For each value in `nums`, the function determines the number of primes up
      to that number and uses this count to decide the round winner based on
      its parity (odd or even).
    - Returns the overall winner of the game by comparing the total rounds won
      by each player, or `None` in case of a tie.
    """
    if x < 1 or not nums:
        return None

    n = max(nums)

    primes = is_prime_sieve(n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_left = sum(primes[2:n + 1])
        if primes_left % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'


# if __name__ == "__main__":
# print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
