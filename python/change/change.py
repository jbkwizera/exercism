import sys
sys.setrecursionlimit(1500)

def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("Change must be nonnegative.")
    elif target and target < coins[0]:
        raise ValueError("Change must be at least the smallest coin.")
    if target == 0:
        return []

    memoize= dict()
    result = find_fewest_coins_helper(coins, target, memoize)
    if result[0] == 0:
        raise ValueError("Change cannot be obtained.")
    return result

def find_fewest_coins_helper(coins, target, memoize):
    change = [0]*1000
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
