def some_decorator(arg=None):
    def decorator(func):
        def wrapper(*a, **ka):
            return func(*a, **ka)
        return wrapper

    if callable(arg):
        return decorator(arg) # return 'wrapper'
    else:
        return decorator # ... or 'decorator'
    
    

@some_decorator()
def some_method():
    pass