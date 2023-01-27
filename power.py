
def power(number, power):
    result = 1
    for _ in range(0, power):
        result *= number
    return result

print(" Result of power(2, 15):", power(2,15))
print(" Result of 2**15:       ", 2**15)
