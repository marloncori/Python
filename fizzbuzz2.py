
def fizzbuzz(number):
    numbers = []
    for i in range(1, number+1):
        if i == 1:
            numbers.append(str(i))
        elif i % 3 == 0:
            numbers.append("fizz")
        elif i % 5 == 0:
            numbers.append("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            numbers.append("fizzbuzz")
        else:
            numbers.append(str(i))
    return numbers

print(" Result: ", fizzbuzz(20))
