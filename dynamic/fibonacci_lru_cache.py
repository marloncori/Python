from time import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    try:
        start = time()
        for i in range(30):
            print(fib(i))
        end = time()
        elapsed_time = end - start
        print("\n Program execution took {:.2f} milliseconds.".format(elapsed_time))

    except (KeyboardInterrupt, SystemExit):
        print(" Program has been stopped.")


