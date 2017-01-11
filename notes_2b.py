from collections import OrderedDict
registry = OrderedDict()

class MultiMethod(object):
    def __init__(self, name):
        self.name = name
        self.typemap = OrderedDict()

    def __call__(self, *args):
        types = tuple(arg.__class__ for arg in args)
        function = self.typemap.get(types)
        if function is None:
            for target_types, func in self.typemap.items():
                try:
                    for idx, target_type in enumerate(target_types):
                        target_type(types[idx])
                    return func(*args)
                except:
                    pass
            else:
                raise TypeError("no match")
        return function(*args)

    def register(self, types, function):
        if types in self.typemap:
            raise TypeError("duplicate registration")
        self.typemap[types] = function


def multimethod(*types):
    def register(function):
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = MultiMethod(name)
        mm.register(types, function)
        return mm
    return register


@multimethod(int, int)
def foo(a, b):
    print("int")
    return a + b


@multimethod(float, float)
def foo(a, b):
    print("float")
    return a + b


@multimethod(str, str)
def foo(a, b):
    print("str")
    return a[0], b[0]

if __name__ == '__main__':
    print(registry)
    foo(1.0, 2.0)
    foo(1, 2)
    foo("1", "2")
    foo(1.5, 2)
    # foo([], [])
