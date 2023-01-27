lista = [0, 1, 2, 3, 4, 5, 7]
lista2 = [0, 1, 2, 3, 4, 5, 7, 8]

def list_half(x):
    if len(x)%2 != 0:
        even_len = len(x) - 1
        middle = (even_len // 2)
        return x[middle]
    else:
        return "Length of list should be equal to an uneven number."

print(list_half(lista))
print(list_half(lista2))

print(lista)

def head(x):
    return x[0]

def tail(x):
    return x[1:]

def last(x):
    return x[-1]

def nolast(x):
    return x[:-1]

def before_last(x):
    return x[-2]

print(head(lista))
print(tail(lista))
print(last(lista))
print(nolast(lista))
print(before_last(lista))

def rev(x):
    n = []
    if x:
        for _ in range(len(x)):
            n.append(x.pop())
        return n
    return " List is empty!"

print(rev(lista))
w = []
print(rev(w))
















