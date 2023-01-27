
def quick_sort(arr, left, right):
    index = (left+right)//2
    pivot = arr[index]
    start = left
    end = right
    while start <= end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start <= end:
            aux = arr[start]
            arr[start] = arr[end]
            arr[end] = aux
            start += 1
            end -= 1
    if end > left:
        quick_sort(arr, left, end)
    if start < right:
        quick_sort(arr, start, right)
    return arr

lista = [98,8,32,3,42,342,59,8,53,45,86,90,10]
print(quick_sort(lista, 0, len(lista)-1))
print(lista)
