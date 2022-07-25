def some_decorator():
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

@some_decorator()
def some_method():
    pass