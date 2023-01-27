from time import sleep

numbers = [34, 56, 12, 5, 97, 43, 87, 103]

def swap(first, second):
    elems = [second, first]
    yield elems

def sort(lista):
    nums = []
    length = len(lista)
    for i in range(len(lista)):
        while lista[i+1] < len(lista)-1:
            if lista[i] > lista[i+1]:
                nums.append(swap(lista[i], lista[i+1]))
                nums.append(swap(lista[i], lista[i+1]))
                print(nums)
                sleep(1)
            else:
                nums.append(lista[i])
                nums.append(lista[i+1])
                print(nums)
                sleep(1)
            length -= 1
    return nums

print(swap(numbers[0], numbers[1]))
print(swap(numbers[0], numbers[1]))
