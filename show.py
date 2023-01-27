
def print_result(func):
    def inner(args):
        print(args)
        return print(func(args))
    return inner

def show_result(func):
    def inner(*args, **kwargs):
        print(*args, **kwargs)
        return print(func(*args, **kwargs))
    return inner
