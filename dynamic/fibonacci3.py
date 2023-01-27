from time import time

def cached(func):
    cache = {}
    def worker(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return worker

@cached
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

