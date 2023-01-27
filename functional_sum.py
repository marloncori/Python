import itertools

y =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(y))

for x in itertools.count():
    print(x)
    if x == 100:
        break

