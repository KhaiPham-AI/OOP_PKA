def logged(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        parameters = ", ".join([repr(arg) for arg in args] + [f"{key}={value!r}" for key, value in kwargs.items()])
        result = func(*args, **kwargs)
        print(f"you called {func_name}({parameters})")
        print(f"it returned {result}")
        return result
    return wrapper

@logged
def func(*args):
 return 3 + len(args)
print(func(4, 4, 4))

@logged
def sum_func(a, b):
 return a + b
print(sum_func(1, 4))