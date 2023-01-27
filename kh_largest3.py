# https://www.youtube.com/watch?v=Peq4GCPNC5c&t=2279s
# FreeCodeCamp - 10 Common Coding Interview Problems
# 3 - kth largest number (29-05-2022) 'danger', 'garden'
# T(n) = 2n + (k - 1) * logn + logn = O(n + klogn), S(n) = O(n)
# third approach, now with a priority queue
###########################################################
import heapq

def kth_largest(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)

###########################################################
def show_result(output, query):
    if output == None:
        print(f'\n\t The output parameter is empty!')
        return
    
    if output != -1:
        print(f'\n\t Given the target {query}, the kth largest\n\t number in the array is {output}.')
    else:
        print(f'\n\t An error has happened. There is no result to be showed.')
        
###########################################################
def run_test():
    array = [2, 4, 2, 9, 7, 5, 6, 7, 1, 3]
    k = 4 # first = 9, sec = 7, thrid = 7, fourth = 6
    output = kth_largest(array, k)
    show_result(output, k)
    
###########################################################
def cleanup():
    print(' User has stopped program execution. Goodbye!')

###########################################################
if __name__ == '__main__':
    try:
        run_test()    
        
    except (KeyboardInterrupt, SystemExit):
        cleanup()
###########################################################