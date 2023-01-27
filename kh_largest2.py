###########################################################
# https://www.youtube.com/watch?v=Peq4GCPNC5c&t=2279s
# FreeCodeCamp - 10 Common Coding Interview Problems
# 3 - the Kth largest element problem (29-05-2022) 'danger', 'garden'
# T(n, k) = 0(nlogn), S(n) = O(n)
#
# You have been given an array of integers Arr and an integer
# k, find the kth largest element --> 1 <= k <= arr[-1]
###########################################################
def quick_sort(arr, left, right):
    index = (left+right)//2
    pivot = arr[index]
    start = left; end = right
    while start <= end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start <= end:
            aux = arr[start]
            arr[start] = arr[end]
            arr[end] = aux
            start += 1; end -= 1
    if end > left:
        quick_sort(arr, left, end)
    if start < right:
        quick_sort(arr, start, right)
    
def kth_largest(arr, k):
    n = len(arr)
    quick_sort(arr, 0, n-1)
    return arr[n-k]

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
    k = 5 # first = 9, sec = 7, thrid = 7, fourth = 6
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