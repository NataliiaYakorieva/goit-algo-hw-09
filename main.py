from typing import Dict, List


def find_coins_greedy(amount: int, coins: List[int]) -> Dict[int, int]:
    """
    Returns a dictionary with the number of coins of each denomination
    to make up the given amount using a greedy algorithm.

    Args:
        amount (int): The amount to be changed.
        coins (List[int]): List of available coin denominations.

    Returns:
        Dict[int, int]: A dictionary where keys are coin denominations and values are their counts.
    """
    result: Dict[int, int] = {}

    for coin in sorted(coins, reverse=True):
        count = amount // coin
        if count:
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount: int, coins: List[int]) -> Dict[int, int]:
    """
    Returns a dictionary with the number of coins of each denomination
    to make up the given amount using dynamic programming (minimum number of coins).

    Args:
        amount (int): The amount to be changed.
        coins (List[int]): List of available coin denominations.

    Returns:
        Dict[int, int]: A dictionary where keys are coin denominations and values are their counts.
    """
    min_coins = [0] + [float('inf')] * amount
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin
    result: Dict[int, int] = {}
    i = amount

    while i > 0:
        coin = last_coin[i]
        result[coin] = result.get(coin, 0) + 1
        i -= coin
    return result


if __name__ == "__main__":
    # Example 1: Custom coin set [1, 3, 4], amount = 6
    coins_custom = [1, 3, 4]
    test_amount_custom = 6
    print("Custom coin set [1, 3, 4], amount = 6")
    print(
        "Greedy:",
        find_coins_greedy(
            test_amount_custom,
            coins_custom)) # {4: 1, 1: 2}
    print(
        "DP:",
        find_min_coins(
            test_amount_custom,
            coins_custom),
        '\n') # {3: 2}

    # Example 2: Standard coin set [50, 25, 10, 5, 2, 1], amount = 113
    coins_standard = [50, 25, 10, 5, 2, 1]
    test_amount_standard = 113
    print("Standard coin set [50, 25, 10, 5, 2, 1], amount = 113")
    print(
        "Greedy:",
        find_coins_greedy(
            test_amount_standard,
            coins_standard)) # {50: 2, 10: 1, 2: 1, 1: 1}
    print("DP:", find_min_coins(test_amount_standard, coins_standard)) # {50: 2, 10: 1, 2: 1, 1: 1}
