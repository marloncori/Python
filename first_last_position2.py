###########################################################
# https://www.youtube.com/watch?v=Peq4GCPNC5c&t=2279s
# FreeCodeCamp - 10 Common Coding Interview Problems
# 2 - First and last position problem (29-05-2022)
# T(n) = 2 * O(logn) = O(logn), S(n) = O(1) thanks to int vars
#
# Given a sorted array of integers Arr and an integer
# target find the index of the first and last position
# of target in Arr. If target can't be found in Arr,
# then return [-1, -1]
# Version with binary_search(list)
###########################################################
def first_binary_search(arr, query):
    if arr[0] == query:
        return 0
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == query and arr[mid-1] < query:
            return mid
        elif arr[mid] < query:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def last_binary_search(arr, query):
    if arr[-1] == query:
        return len(arr)-1
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == query and arr[mid+1] > query:
            return mid
        elif arr[mid] > query:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def first_and_last(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    start = first_binary_search(arr, target)
    end = last_binary_search(arr, target)
    return [start, end]

def show_result(output, query):
    if len(output) == 0:
        print(f'\n\t The output parameter is empty!')
        return
    
    if output[0] != -1:
        print(f'\n\t The target number {query} has been found \n\t in positions {output[0]} and {output[1]}.')
    else:
        print(f'\n\t The target number {query} has not been found in array!')

###########################################################
def run_test_A():
    array = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    query = 5
    output = first_and_last(array, query)
    show_result(output, query)

def run_test_B():
    array = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    query = 3
    output = first_and_last(array, query)
    show_result(output, query)
    
def cleanup():
    print(' User has stopped program execution. Goodbye!')

###########################################################
if __name__ == '__main__':
    try:
        run_test_A()    
        run_test_B()
        
    except (KeyboardInterrupt, SystemExit):
        cleanup()
###########################################################