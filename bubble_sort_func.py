
###############################################################################
def show_result(func):
    def inner(args):
        print(args)
        return print(func(args))
    return inner

###############################################################################

@show_result
def bubble_sort(z):
    for i in range(len(z)):
        for j in range(len(z)-i-1):
            if z[j] > z[j+1]:
                tp = z[j]
                z[j] = z[j+1]
                z[j+1] = tp
    return z

lista = [45, 21, 34, 67, 98, 76, 43, 21, 15]
bubble_sort(lista)
