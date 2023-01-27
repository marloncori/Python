def swap(first, second):
    temp = first
    first = second
    second = temp

def partition(data, begin, end):
    pivot = data[begin]
    count = 0
    for i in range(begin+1, end):
        if data[i] == pivot:
            count += 1

    pivotId = begin + count
    swap(data[pivotId], begin)
    i = begin
    j = end
    while i < pivotId and j < pivotId:
        while data[i] <= pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i < pivotId and j > pivotId:
            i += 1
            j -= 1
            swap(data[i], data[j])

    return pivotId

def quick_sort(data, begin, end):
    if begin > end:
        return
    index = partition(data, begin, end)
    quick_sort(data, begin, index-1)
    quick_sort(data, index+1, end)

def show_array(data, mode=0):
    msg = ""
    match mode:
        case 0:
            msg = "unsorted"
        case 1:
            msg = "sorted"
    print(f'\n This is the {msg} array:\n\t[')
    for x in data:
        print(x, end=" ")
    print("].")

    
def test():
    nums = [34, 56, 78, 90, 43, 21, 3, 102, 15]
    show_array(nums)
    start = 0
    end = len(nums)-1

    mode = 1
    quick_sort(nums, start, end)
    show_array(nums, mode)


if __name__ == '__main__':
    try:
        test()
    except (KeyboardInterrupt, SystemExit):
        print(" Program has been interrupted")
