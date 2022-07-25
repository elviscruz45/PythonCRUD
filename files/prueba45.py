def some_decorator(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(arg1)
            print(arg2)
            return func(*args, **kwargs)
        return wrapper
    return decorator




@some_decorator('hello', 'bye')
def some_method():
    pass