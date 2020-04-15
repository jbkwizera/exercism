import sys
sys.setrecursionlimit(1500)

def find_fewest_coins(coins, target):
    change = [1]*1000
    if target == 0:
        return []
    elif target in coins:
        return [target]
    else:
        for coin in [coin for coin in coins if coin <= target]:
            change = min(
                [change, [coin]+find_fewest_coins(coins, target-coin)],
                key=lambda val: len(val)
            )
        return change
