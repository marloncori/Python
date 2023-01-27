from show import show_result

def partition(ys, begin, end):
    pivot = ys[end]
    i = begin - 1
    for j in range(begin, end):
        if ys[j] <= pivot:
            i+=1
            temp  = ys[i]
            ys[i] = ys[j]
            ys[j] = temp
    temp = ys[i+1]
    ys[i+1] = ys[end]
    ys[end] = temp
    return i+1
        
        
@show_result
def quick_sort(xs, begin, end):
    if begin < end:
        partition_index = partition(xs, begin, end)

        quick_sort(xs, begin, partition_index-1)
        quick_sort(xs, partition_index+1, end)


zs = [32, 76, 43, 54, 21, 43, 23, 17, 98, 87, 54, 65, 98]
quick_sort(zs, 0, len(zs)-1)
