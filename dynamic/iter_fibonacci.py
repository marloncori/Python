from time import time

def iter_fib(n):
    series = [1, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[-1]

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



