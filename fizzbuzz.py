
def print_numbers():
    for i in range(1,101):
        if i % 3 == 0:
            print("\t Fizz!")
        elif i % 5 == 0:
            print("\t Buzz!")
        elif i % 3 == 0 and i % 5 == 0:
            print("\t FizzBuzz!")
        else:
            print(" ==> ", i)

print_numbers()
