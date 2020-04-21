import copy

UNIT_COST = 800
DISCOUNTS = [0, 0, 5, 10, 20, 25]
DISCOUNT_COST = [UNIT_COST*(100-DISCOUNT)/100 for DISCOUNT in DISCOUNTS]

def total(basket):
    if not basket:
        return 0
    else:
        books = books_count(basket)
        best_deal = sum(books)*UNIT_COST
        for grouping in partitions(sum(books)):
            if is_valid_grouping(grouping, books):
                best_deal = min(best_deal, grouping_amount(grouping))
        return best_deal

def books_count(basket):
    books = [0]*6
    for book_type in basket:
        books[book_type] += 1
    return books

def partitions(n):
    a = [0 for i in range(n + 1)]
    k = 1
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        yield a[:k + 1]

def is_valid_grouping(grouping, books):
    _books = sorted(copy.deepcopy(books), reverse=True)
    for group in reversed(grouping):
        type_count = 0
        for i in range(len(_books)):
            if type_count != group and _books[i]:
                _books[i] -= 1
                type_count+= 1
        if type_count != group:
            return False
    return True

def grouping_amount(grouping):
    amount = 0
    for group in grouping:
        amount += group*DISCOUNT_COST[group]
    return amount
