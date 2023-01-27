
def sq_root(number):
    result = number**(1/2)
    return result

def cb_root(number):
    result = number**(1/3)
    return result

def qd_root(number):
    result = number**(1/4)
    return result

print(" Result of sqrt(81):", int(sq_root(81)))
print(" Result of cbrt(27):", int(cb_root(27)))
print(" Result of qdrt(32):", int(qd_root(32)))
