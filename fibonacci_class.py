
class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, \n  got "{n}"')

        if n < len(self.cache):
            return self.cache[n]
        else:
            fib_number = self(n-1) + self(n-2)
            self.cache.append(fib_number)
        return self.cache[n]


fibonacci_of = Fibonacci()
print([fibonacci_of(n) for n in range(20)])
