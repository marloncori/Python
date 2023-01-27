from time import sleep, time

fib_cache = {}
def fib(n):
    if n <= 2:
        return 1
    if n not in fib_cache:
        fib_cache[n] = fib(n-1) + fib(n-2)
    return fib_cache[n]

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
