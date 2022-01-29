class nth_fibonacci_memoized:
    def __init__(self):
        self.memo = {}

    def nth_fibonacci(self, n):
        # Edge case
        if n < 0:
            raise Exception('Can\'t be negative')
        
        # Base cases
        if n in [1, 0]:
            self.memo[n] = n
            return n

        # Memoize
        if n in self.memo:
            return self.memo[n]

        # Recursion
        result = self.nth_fibonacci(n - 1) + self.nth_fibonacci(n - 2)

        self.memo[n] = result

        return result

    def nth_fibonacci_iterative(self, n):
        # Edge case
        if n < 0:
            raise Exception('Can\'t be negative')

        if n in [1, 0]:
            return n

        previous = 0
        current = 1

        for _ in range(n - 1):
            temp = current
            current = previous + current
            previous = temp

        return current

nth_fibonacci_memoized = nth_fibonacci_memoized()

print(nth_fibonacci_memoized.nth_fibonacci(5))