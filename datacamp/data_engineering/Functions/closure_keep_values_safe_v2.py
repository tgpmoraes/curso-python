def my_special_function():
    print('You are running my_special_function()')


def get_new_func(func):
    def call_func():
        func()
    return call_func


new_func = get_new_func(my_special_function)

# Delete my_special_function()
del(my_special_function)

new_func()
