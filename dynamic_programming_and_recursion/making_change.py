class Tupac:
    def __init__(self):
        self.memo = {}

    def making_change(self, amount, denominations, current_index = 0):
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

        memo_key = str((amount, current_index))

        if memo_key in self.memo:
            print('I see no changes for:', amount, current_index)
            return self.memo[memo_key]

        print('Checking ways to make %i with %s' % (amount, denominations[current_index:]))

        current_coin = denominations[current_index]

        # See how many possibilities exist for each number of times
        possibilities = 0

        while amount >= 0:
            possibilities += self.making_change(amount, denominations, current_index + 1)
            amount -= current_coin

        self.memo[memo_key] = possibilities
        return possibilities

amount = 4
denominations = [1, 2, 3]

shakur = Tupac()

print(shakur.making_change(amount, denominations))