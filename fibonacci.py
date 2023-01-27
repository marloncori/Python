
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))    

def recur_fibo(n):
    if n in {0, 1}:
        return n
    return recur_fibo(n-1) + recur_fibo(n-2)


for i in range(20):
    print(fibonacci(i), end=" ")

print("\n")

for x in range(10):
    print(recur_fibo(x), end=" ")

print("\n")

def cached_fibo(n):
    cache = {0: 0, 1: 1}
    if n in cache:
        return cache[n]
    cache[n] = cached_fibo(n-1) + cached_fibo(n-2)
    return cache[n]

print([cached_fibo(y) for y in range(15)])
