class Foo(object):
    
    def __init__(self, x):
        self._x = x

    def __format__(self,casa):
        return '<Foo x={0}>'.format(self._x)
    

foo = Foo(12)

# Pass "baz" as a format_spec
print("This is a foo: {0:baz}".format(foo))

print("This is a foo: {0}".format(foo))
