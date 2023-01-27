# test
num = None

if not num:
    print(" null")

val = 7
if val:
    print(" --> ", val)

def is_null(x):
    return not x

print(is_null(val))

print(is_null(num))

def is_greater(x, y):
    return x > y

num2 = 10
print(is_greater(num2, val))
