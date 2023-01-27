
def fact(n):
    if n > 0: return n * fact(n-1)
    return 1

print(fact(0))

def add(x):
    if x: return x[0] + add(x[1:])
    return 0

def sub(x):
    if x: return x[0] - add(x[1:])
    return 0

def mul(x):
    if x: return x[0] * add(x[1:])
    return 0

def div(x):
    if x: return x[0] / add(x[1:])
    return 0

def half(x, first_half=False):
    if len(x)%2 == 0:
        half = len(x)//2
        if first_half:
            return x[0:half]
        else:
            return x[half:]
    return "Length is uneven. Cannot calculate half."


y = [0, 1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 14]

print(add(y))
print(sub(y))
print(mul(y))
print(div(y))
print(half(y))
print(half(y, True))

def evens(xs):
    nums = []
    if xs:
        for x in xs:
            if x%2 == 0: nums.append(x)
        return nums
    
print(evens(y))

def unevens(xs):
    nums = []
    if xs:
        for x in xs:
            if x%2 != 0: nums.append(x)
        return nums

print(unevens(y))    
