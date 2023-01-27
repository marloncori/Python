
def binary_search(nums, inf, sup, query):
    mid = 3
    found = False

    while inf <= sup:
        if nums[mid] == query:
            found = True
            break
        if nums[mid] > query:
            sup = mid
            mid = (sup+inf)//2
        if nums[mid] < query:
            inf = mid
            mid = (sup+inf)//2

    if found:
        return mid
    return -1
##########################################

if __name__ == '__main__':
    try:
        numbers = [3, 4, 5, 6, 7, 8, 9]
        print("\n This is the list of numbers: [ ", end="")
        for num in numbers:
            print(num, end= " ")    
        print("]")
        begin = 0
        end = 6
        query = 8
        result = binary_search(numbers, begin, end, query)
        if result == -1:
            print("\n The searched number has not been found.")
        else:
            print(f"\n\t The number {query} was found at position {result}.")
    except KeyboardInterrupt:
        print(" Program has ended.")
            
