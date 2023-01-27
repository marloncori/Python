import math
from time import sleep

def jumpSearch(arr, x, n):
    # Finding block size to be jumped
    step = math.sqrt(n)

    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while(arr[int(min(step, n) - 1)] < x):
        prev = step
        step += math.sqrt(n)
        if (prev >= n):
            return -1
    
    # Doing a linear search for x in block
    # beginning with prev.
    while (arr[int(prev)] < x):
        prev += 1
        # If we reached next block or end of
        # array, element is not present.
        if (prev == int(min(step, n))):
            return -1

    # If element is found
    if (arr[int(prev)] == x):
        return int(prev)

    return -1

def start_search():
    arr = [0, 7, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    size = len(arr)

    # Find the index of 'x' using Jump Search
    for num in arr:
        index = jumpSearch(arr, num, size)
        # Print the index where 'x' is located
        print("\n Number {} is at index {}\n.".format(num, index))
        sleep(1)

if __name__ == '__main__':
    start_search()






    
