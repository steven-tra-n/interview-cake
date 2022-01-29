def making_change(amount, denominations, current_index = 0):
    # Base cases
    # Perfect match
    if amount == 0:
        return 1

    # Too much coin
    if amount < 0:
        return 0

    # Ran out of coin
    if current_index == len(denominations):
        return 0

    print('Checking ways to make %i with %s' % (amount, denominations[current_index:]))

    current_coin = denominations[current_index]

    # See how many possibilities exist for each number of times
    possibilities = 0

    while amount >= 0:
        possibilities += making_change(amount, denominations, current_index + 1)
        amount -= current_coin

    return possibilities

amount = 4
denominations = [1, 2, 3]

print(making_change(amount, denominations))