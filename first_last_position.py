# https://www.youtube.com/watch?v=Peq4GCPNC5c&t=2279s
# FreeCodeCamp - 10 Common Coding Interview Problems
# 2 - First and last position problem (29-05-2022)
# T(n) = O(n), S(n) = O(1)
#
# Given a sorted array of integers Arr and an integer
# target find the index of the first and last position
# of target in Arr. If target can't be found in Arr,
# then retur [-1, -1]
#
###########################################################
def first_and_last(arr, target):
    for x in range(len(arr)):
        if arr[x] == target:
            start_position = x
            while x + 1 < len(arr) and arr[x + 1] == target:
                x += 1
            return [start_position, x]
    return [-1, -1]

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