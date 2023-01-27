
def show(func):
    def inner(args):
        print(args)
        return print(func(args))
    return inner

@show
def insert_sort(sortable_list):
    for this_elem in range(1, len(sortable_list)):
        acc = sortable_list[this_elem]
        previous_elem = this_elem - 1
        while previous_elem >= 0 and acc < sortable_list[previous_elem]:
            sortable_list[previous_elem+1] = sortable_list[previous_elem]
            previous_elem -= 1
        sortable_list[previous_elem+1] = acc
    return sortable_list 

x = [87, 100, 12, 34, 21, 67, 33, 90, 5]
insert_sort(x)
        
