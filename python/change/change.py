import sys
sys.setrecursionlimit(1500)

def find_fewest_coins(coins, target):
    memoize = dict()
    if target == 0:
        return []
    return find_fewest_coins_helper(coins, target, memoize)

def find_fewest_coins_helper(coins, target, memoize):
    change = [1]*1000
    if target in coins:
        memoize[target] = [target]
        return [target]
    elif target in memoize:
        return memoize[target]
    else:
        for coin in [coin for coin in coins if coin <= target]:
            change = min(
                [change, [coin]+find_fewest_coins_helper(coins, target-coin, memoize)],
                key=lambda val: len(val)
            )
            memoize[target] = change
        return change
