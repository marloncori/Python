
def addOne(z):
    return z

def addTwo(y, z):
    return y + addOne(z)

def add(x, y, z):
    return x + addTwo(y, z)

print(add(2, 3, 1))
