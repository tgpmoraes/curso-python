import inspect


def print_args(func):
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs).arguments
        str_args = ', '.join(['{}={}'.format(k, v) for k, v in bound.items()])
        print('{} was called with {}'.format(func.__name__, str_args))
        return func(*args, **kwargs)
    return wrapper


def my_function1(a, b, c):
    print(a + b + c)


# Decorate my_function() with the print_args() decorator
my_function = print_args(my_function1)

my_function(1, 2, 3)

# Decorate my_function() with the print_args() decorator


@print_args
def my_function2(a, b, c):
    print(a + b + c)


my_function2(1, 2, 3)
