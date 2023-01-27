from time import time

def iter_fib(n):
    prev = 1
    curr = 1
    for i in range(n-2):
        next_one = curr + prev
        prev, curr = curr, next_one
    return curr

if __name__ == '__main__':
    try:
        start = time()
        for i in range(30):
            print(iter_fib(i))
        end = time()
        elapsed_time = end - start
        print("\n Program execution took {:.2f} milliseconds.".format(elapsed_time))

    except (KeyboardInterrupt, SystemExit):
        print(" Program has been stopped.")


