from time import time

def fib(n):
    if n <= 2:
        return 1
    if not hasattr(fib, 'cache'):
        fib.cache = {}
    if n not in fib.cache:
        fib.cache[n] = fib(n-1) + fib(n-2)
    return fib.cache[n]

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
